# Roadmap

## Destination

A portfolio project: an appointment booking system for a single beauty clinic,
deployed and publicly reachable, with a clean codebase, tests, and CI from the
first commit. Security and privacy are prepared from the start so the project
could later be adapted for real use.

This is a rewrite of a first version built in Flask. No code is carried over.

## Stack

- FastAPI, Jinja2 templates, HTMX
- SQLAlchemy 2.0, Alembic, PostgreSQL
- Python 3.12, managed with uv
- Ruff (lint and format), mypy in strict mode, pre-commit
- pytest with coverage, run against a real PostgreSQL
- GitHub Actions (`ci.yml`): lint, format check, type check, tests on every
  push and pull request
- Docker and Docker Compose from the first slice (app, PostgreSQL, Mailpit)
- Deploy: Render (app) and Neon (PostgreSQL), deployed automatically from
  `main` after CI passes
- Charts: Chart.js loaded in the page, fed by a JSON endpoint
- i18n: Portuguese, English, French

mypy strict rules may be relaxed case by case, each exception explicit.

## Slices

Every slice ends deployed and visible in production.

| # | Slice | Visible in production | Status |
|---|---|---|---|
| 1 | Skeleton and deploy: uv, Ruff, mypy, pre-commit, CI, Docker, Alembic, i18n, Render + Neon, automatic deploy | Home page in pt/en/fr and `/health` | not started |
| 2 | Login (owner and staff) and services management | Admin with login; services with price | not started |
| 3 | Availability calculation, with tests | Public page showing free slots | not started |
| 4 | Public booking and "request received" email | A client can book | not started |
| 5 | Admin agenda: list and confirm, with email | The clinic confirms bookings | not started |
| 6 | Cancel (with reason) and reschedule, with emails | Full appointment lifecycle | not started |
| 7 | Owner overriding the rules, with explicit warning | Owner can fit extra appointments | not started |
| 8 | Financial and statistics dashboard | Revenue and charts | not started |
| 9 | Portfolio README and demo data | Project ready to show | not started |

## Decisions to take during a slice

- **Slice 2:** how a recruiter accesses the admin (proposal on the table: demo
  accounts with credentials in the README and data reset periodically).
- **Slice 4:** which email provider is used in production. Until then,
  production emails are only written to the log; development uses Mailpit.

## ADR candidates

Decisions with impact that should become ADRs, written with the `/adr` skill:

- Jinja2 + HTMX for the frontend
- Render for the app and Neon for the database (requires checking the
  providers' documentation for the facts the record states)
- Storing times in UTC and converting to the clinic time zone at one point
- Storing the service price on each appointment
- Rescheduling as a cancellation with reason `rescheduled`, without a separate
  status

## Deferred (not in the MVP)

- Attendance marking (completed / no-show)
- Email reminders before the appointment
- Cancellation by the client through email
- Data export (CSV / Excel)
- Full audit log
- Per-appointment price changes (discounts)
- Wider permissions for staff (such as overriding rules)
