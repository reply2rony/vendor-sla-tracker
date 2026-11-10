# Vendor SLA Tracker — Guide

A starter guide for tracking vendor service-level agreements in a
small IT team. This is a learning template — adapt the steps to your
own organisation's contracts. All vendors, services, targets, and
results below are fictional.

## What an SLA is

A service-level agreement is the written promise a vendor makes
about a service: how available it will be, how fast they respond
when it breaks, and how fast they fix it. The tracker keeps those
promises in one place so nobody has to remember them — or argue
about them later.

## The five fields that matter

- **Vendor and service** — who provides it, and what the service
  is. One row per service, not per vendor.
- **Target** — the promised number, written exactly as the contract
  states it (for example, "99.5% uptime" or "respond within 4 hours").
- **Measured result** — what actually happened in the review
  period, measured the same way every time.
- **Status** — met, missed, or at risk. "At risk" means the trend
  points at a miss even if the target has not been missed yet.
- **Review date** — the next date this service is reviewed. A
  service with no review date is a service nobody is watching.

## The monthly review rhythm

1. **Collect the numbers** — for each service, write the measured
   result next to the promised target in `vendor-sla-tracker.csv`.
2. **Flag the misses first** — run the summary script and read the
   missed targets before anything else.
3. **Check the reviews coming due** — a service whose review date
   is this week needs its numbers ready before the meeting.
4. **Record what was agreed** — for every miss, write the vendor's
   response and the agreed fix in the notes column.

## When a vendor misses a target

- **Record it the same day** — a miss recorded late is a miss that
  gets disputed.
- **Tell the vendor in writing** — quote the target, the measured
  result, and the dates.
- **Agree one fix and one date** — "we will improve" is not a fix;
  a named change and a date is.
- **Watch the next period** — a second miss in a row is a pattern,
  not bad luck, and should go to the team lead.
- **Keep the penalty simple** — if the contract promises a credit
  for a miss, claim it in writing and record it in the log.

## Common mistakes (starter notes)

- Tracking the vendor but not the service — one vendor can run
  three services with three different targets.
- Measuring differently each month, so the numbers cannot be
  compared.
- Writing "met" without a measured result to back it up.
- Letting review dates pass without a review.
- Recording real vendor names, contract values, or account details
  in a shared template.
- Treating a target as a guarantee — an SLA is a promise with a
  remedy, not a promise that nothing will ever break.

## Adding your own vendors

Add a row to `vendor-sla-tracker.csv` with: vendor, service,
sla_target, measured_result, status, review_date, contact, and
notes. Keep every entry fictional in samples — never commit real
vendor names, contract values, or account details.

## Sample / Demo notice

All vendors here are fictional samples for learning, labelled
"Sample / Demo" in the diagram. This template does not claim any
production use.
