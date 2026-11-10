# Vendor SLA Tracker — Starter Template

A starter learning template for tracking vendor service-level
agreements (SLAs) in a small IT team: which vendor promised what,
whether they met it, and what happens when they do not. It is a
tracker plus a small SLA log in CSV form, so an IT team can practise
reviewing vendor performance on made-up examples before ever
applying it to a real contract. Sample content only — no real company
data, no real vendors, no invented metrics, and no claim of
production use.

## What it is

- `docs/sla-guide.md` — the guide: how to read an SLA, the key
  terms to track, a review rhythm, and what to do when a vendor
  misses a target.
- `vendor-sla-tracker.csv` — the SLA log in CSV form, so you can
  copy it, filter it, and add your own sample vendors.
- `scripts/sla-summary.py` — a starter Python script that
  summarises the log by vendor and service, and flags missed targets
  and services due for review. Labelled a starter learning template;
  it is not a production tool.

## How to use

1. Add one row per vendor service in `vendor-sla-tracker.csv` —
   vendor, service, the promised target, the measured result, and
   the review date.
2. Once a month, run the summary script and read the flags:
   missed targets first, then reviews coming due.
3. For a missed target, follow the steps in `docs/sla-guide.md` —
   record the miss, tell the vendor, and agree a fix before the
   next review.
4. Summarise the log from the command line:

```bash
python3 scripts/sla-summary.py vendor-sla-tracker.csv
python3 scripts/sla-summary.py vendor-sla-tracker.csv --status missed
python3 scripts/sla-summary.py vendor-sla-tracker.csv --vendor "Sample Internet Provider"
```

## Key SLA terms (starter guide)

| Term | Meaning |
|------|---------|
| Uptime target | The share of time a service should be available |
| Response time | How quickly the vendor must first reply to a fault |
| Resolution time | How quickly the vendor must fix a fault |
| Review date | When the service is next reviewed |
| Penalty / credit | What the vendor owes if a target is missed |

Terms above are starter definitions for a learning template, not
legal advice and not a standard for any real contract.

## Sample / Demo notice

All vendors, services, targets, and results in this repo are
fictional samples for learning. The diagram in `docs/diagram.png`
is a locally generated illustration labelled "Sample / Demo" — it
is not a screenshot of a real system, and this template does not
claim any production use.

## License

MIT — see `LICENSE`.
