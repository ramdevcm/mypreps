# S3 Architecture Deep Dive

## 1. Partitioning

- S3 partitions the keyspace **by key prefix**. Ranges of keys are assigned to partitions, which are spread across the fleet.
- When request rate or data in a prefix range grows, S3 **automatically splits** the partition into smaller ranges and redistributes them. This is how S3 scales horizontally.
- Throughput scales **per prefix**: at least **3,500 writes/s** and **5,500 reads/s** per prefix.
- The keymap is partitioned the same way, so no single index node becomes a bottleneck.

```plaintext
keyspace:  a......f | g......m | n......s | t......z
            part 1     part 2     part 3     part 4
                          |
                     hot range? --> split --> part 2a | part 2b
```

## 2. Sharding

- An object's bytes are split into shards: data shards plus parity shards from erasure coding.
- Shards are spread across independent storage nodes, racks and AZs, so no single failure domain holds enough of them to matter.
- **Multipart uploads:** each part is sharded and stored on its own, then the index stitches the parts together logically.
- Sharding spreads both the failure risk and the read/write load of one object across the fleet.

## 3. Checksums and integrity

| When | What happens |
|---|---|
| Upload | Bytes are checked against the checksum **before** the PUT is acknowledged, which catches corruption in transit |
| At rest | A background fleet keeps re-reading shards and recomputing checksums to catch bit rot and silent disk corruption |
| Repair | A bad or lost shard is rebuilt from the surviving data and parity shards and rewritten to a healthy node (auto-healing) |
| Download | Checksums are verified again so the client gets exactly what was stored |

Supported algorithms: **CRC32, CRC32C, SHA-1, SHA-256**, plus the ETag (often the MD5 of the content).

## 4. Erasure coding (expanded)

- Reed-Solomon-style coding: split into `k` data shards, compute `m` parity shards, store `n = k + m`. **Any `k` of the `n` rebuild the object.**
- Parameters are chosen so shards can be lost across disks, racks and whole AZs at once while still meeting 11 nines.
- Storage overhead = `n / k` (about **1.5x**) vs **3x** for triple replication.
- **Repair cost:** rebuilding one lost shard means reading `k` surviving shards. That costs CPU and I/O, in exchange for the large storage savings.

## 5. How it fits together on a request

```plaintext
PUT:  client -> front end (auth, route)
             -> checksum bytes
             -> shard + erasure-code
             -> write shards across 3+ AZs
             -> update keymap
             -> ACK

GET:  client -> front end
             -> keymap lookup (key -> shard locations)
             -> fetch k shards (rebuild if any missing)
             -> verify checksums
             -> stream back

BACKGROUND:  integrity scan -> checksum verify -> shard repair
             (runs independently of user requests)
```
