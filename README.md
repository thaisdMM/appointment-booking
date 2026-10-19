# Appointment Booking

Web app for booking a clinic's services online, with an admin area.

## Features

- Clients browse services and prices and book an appointment online.
- The clinic confirms, cancels, and reschedules appointments, with an email to
  the client at each step.
- The owner sees a monthly financial dashboard: revenue, most booked services,
  and cancellations.
- Available in Portuguese, English, and French.

## Status

In development. The project is built in vertical slices, each one deployed
to production; progress is tracked in [docs/roadmap.md](docs/roadmap.md).

## Stack

FastAPI, Jinja2, HTMX, SQLAlchemy, Alembic, PostgreSQL, Docker, GitHub
Actions. Deployed on Render and Neon.

## Running locally

Requires Docker.

1. Copy `.env.example` to `.env` and fill in the values.
2. Start the app, PostgreSQL, and Mailpit:

   ```
   docker compose up --build
   ```

3. Open the app at http://localhost:8002 and the Mailpit inbox at
   http://localhost:8025.

Run the tests:

```
docker compose exec web pytest
```
