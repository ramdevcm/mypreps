# S3: Architect-Level Takeaways

Beyond the mechanics, these are the implications that matter at architect or principal level.

## 1. Consistency model
- Read-after-write has been strongly consistent since 2020, but **LIST operations and cross-region replication are still eventually consistent**.
- Don't design assuming listings are instantly accurate. Know which operations are strong and which are eventual.

## 2. Partition / prefix scaling
- The limit of ~3,500 writes/s and ~5,500 reads/s per prefix is the most common cause of unexplained S3 throttling at scale.
- Design key schemas to spread requests from day one. Retrofitting after you hit the limit is painful.

## 3. Failure domains
- Standard spans 3+ AZs; One Zone-IA does not.
- Choosing between them decides your blast radius (whether you survive an AZ loss), not just your price.

## 4. Durability ≠ availability ≠ recoverability
- 11 nines of durability won't save you from an accidental delete, a bad deploy, or ransomware.
- That's what **versioning, Object Lock, MFA delete and replication** are for. Durability is physics; recoverability is your design.

## 5. Metadata path vs data path
- The keymap and the object bytes are separate systems.
- This explains S3's latency behaviour and why some operations (e.g. LIST vs GET) behave differently.

## 6. Cost architecture
- Request costs, retrieval costs on cold tiers, Glacier early-deletion fees, cross-AZ and egress charges.
- At scale these dwarf the storage bill. **Lifecycle policy design** is a principal-level concern.

## 7. Security model
- Encryption at rest: **SSE-S3, SSE-KMS, SSE-C**.
- Bucket policies vs IAM vs ACLs. Use VPC endpoints to keep traffic off the public internet.
- Public-bucket breaches almost always come from a policy-design failure.
