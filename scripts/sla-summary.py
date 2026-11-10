#!/usr/bin/env python3
"""Starter learning template: summarise the vendor SLA tracker log.

Usage:
    python3 scripts/sla-summary.py vendor-sla-tracker.csv
    python3 scripts/sla-summary.py vendor-sla-tracker.csv --status missed
    python3 scripts/sla-summary.py vendor-sla-tracker.csv --vendor "Sample Internet Provider"

Summarises the CSV by vendor and status, and flags missed targets
and services whose review date is coming due. Sample data only;
no real company data.
"""
import argparse
import csv
import sys
from collections import Counter
from datetime import date, timedelta


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description="Summarise the vendor SLA tracker log.")
    ap.add_argument("csv_file", help="path to vendor-sla-tracker.csv")
    ap.add_argument("--status", help="filter by status (e.g. missed)")
    ap.add_argument("--vendor", help="filter by vendor name")
    args = ap.parse_args()

    try:
        rows = load(args.csv_file)
    except FileNotFoundError:
        print(f"File not found: {args.csv_file}")
        sys.exit(1)

    if args.status:
        rows = [r for r in rows if r.get("status", "").lower() == args.status.lower()]
    if args.vendor:
        rows = [r for r in rows if r.get("vendor", "").lower() == args.vendor.lower()]

    if not rows:
        print("No matching SLA records.")
        sys.exit(0)

    print(f"SLA records: {len(rows)}")
    print()
    print("By status:")
    for st, n in Counter(r.get("status", "") for r in rows).most_common():
        print(f"  {st}: {n}")
    print()
    print("By vendor:")
    for v, n in Counter(r.get("vendor", "") for r in rows).most_common():
        print(f"  {v}: {n}")
    print()
    missed = [r for r in rows if r.get("status", "").lower() == "missed"]
    if missed:
        print("Missed targets — follow up with the vendor first:")
        for r in missed:
            print(f"  {r['vendor']} — {r['service']}: target {r['sla_target']}, "
                  f"measured {r['measured_result']}")
    else:
        print("No missed targets in this view.")
    print()
    today = date.today()
    soon = today + timedelta(days=14)
    due = []
    for r in rows:
        try:
            rd = date.fromisoformat(r.get("review_date", "").strip())
        except ValueError:
            continue
        if today <= rd <= soon:
            due.append((rd, r))
    if due:
        print("Reviews due in the next 14 days:")
        for rd, r in sorted(due, key=lambda t: t[0]):
            print(f"  {rd} — {r['vendor']} ({r['service']})")
    else:
        print("No reviews due in the next 14 days.")


if __name__ == "__main__":
    main()
