# Aurora RTO & RPO

- **RPO (Recovery Point Objective):** the most data loss you can tolerate, measured in time.
- **RTO (Recovery Time Objective):** the most downtime you can tolerate; it drives failover and recovery design.

## RPO

- **In-region:** effectively zero for AZ failures, because the storage layer is synchronous across AZs.
- **Point-in-time recovery:** restores to any second in the retention window. Aurora backs up to S3 continuously.
- **Cross-region (Global Database):** ~1 second, because replication is asynchronous.

## RTO

- **In-region failover to a replica:** ~30–60 s (often under 30 s with a reader ready).
- **No replica, instance restart:** several minutes.
- **Global Database cross-region:** managed planned failover ~1 minute or less; unplanned promotion usually around a minute.

## Rough numbers

| Scope | RPO | RTO |
|---|---|---|
| In-region (with a reader) | ~0 | < 1 min |
| Cross-region | ~1 s | ~1 min |
