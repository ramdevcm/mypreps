# AWS ☁️

How core AWS storage services work behind the scenes: what physically happens to your bytes, and what that means when you design systems on top of them.

## Sections

- **S3**: object storage internals
    - [How S3 Stores Data](./s3/s3.md): namespace, keymap, erasure coding, physical placement
    - [S3 Architecture Deep Dive](./s3/s3-internals.md): partitioning, sharding, checksums, request flow
    - [S3 Architect-Level Takeaways](./s3/s3-architect.md): design implications
- **RDS & Aurora**: relational database storage
    - [RDS vs Aurora](./aurora/rds-vs-aurora.md): coupled vs decoupled storage
    - [Aurora Storage Layer](./aurora/aurora-storage.md): "the log is the database", segments, pages
    - [Aurora Quorum: 6 / 4 / 3](./aurora/aurora-quorum.md): six copies, quorum math, failure cases
    - [Aurora Global Database](./aurora/aurora-global.md): cross-region replication and failover
    - [Aurora RTO & RPO](./aurora/aurora-rto-rpo.md): recovery numbers

## One-line mental models

| Service | Mental model |
|---|---|
| S3 | Distributed key-value store; bytes are erasure-coded and spread across 3+ AZs |
| RDS | Managed EC2 + EBS; replicates a **volume** |
| Aurora | Compute talks to a shared storage fleet; replicates a **log stream** |
