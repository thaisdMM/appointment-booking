# Domain rules

Business rules decided before the modules exist. When a slice creates a module,
the rules that belong to it move into that module's `README.md` and are removed
from this file.

## Clinic

- A single clinic. Its time zone is configured once (`CLINIC_TIMEZONE`,
  default `Europe/Zurich`).
- Every time is stored in UTC and converted to the clinic time zone at a single
  point of the code, both when displaying and when receiving dates.
- Currency is configured once (default CHF). Amounts include cents.

## Roles

- **Owner:** everything staff does, plus managing services and users, seeing
  the financial dashboard, and overriding any scheduling rule.
- **Staff:** sees the agenda, creates bookings for clients, confirms, cancels,
  and reschedules. Staff never overrides a scheduling rule.

## Scheduling rules

- Opening hours: Monday to Friday 09:00–18:00, Saturday 09:00–15:00, Sunday
  closed. No lunch break.
- A configurable buffer applies between any two appointments.
- Minimum notice and maximum booking window are configurable.
- Closed days and holidays are configurable.
- All of the above are configurable by the owner. Defaults carried over from
  the first version: buffer 10 minutes, minimum notice 2 hours, maximum window
  90 days.
- The clinic serves one client at a time: a client can never book a slot that
  overlaps another appointment, whatever the service.
- The owner can override every rule, including overlaps, with an explicit
  warning on screen. There is no limit to how many appointments may overlap.

## Appointment lifecycle

- Statuses: `pending`, `confirmed`, `cancelled`.
- A booking made by a client is created `pending`. When the clinic confirms
  it, it becomes `confirmed` and the client receives an email.
- Cancelling requires a reason: `client_request`, `rescheduled`,
  `clinic_closed`, `no_staff`, `other`, with an optional note.
- Rescheduling cancels the original appointment with reason `rescheduled`,
  linked to the new one. The new appointment is created `confirmed`, and the
  client receives an email.
- Each appointment stores the service price at the moment it was booked.

## Clients

- A client is identified by email, normalized and unique.
- Phone is unique and stored in international format, with Switzerland as the
  default region.
- A booking with a phone already registered under a different email is
  rejected, with a message asking the client to use the original email or to
  contact the clinic.
- The client's language is the language the site was in at booking time. It is
  stored on the client, updated on every booking, and used for emails.

## Emails (MVP)

- Booking received (to the client, on public booking).
- Booking confirmed.
- Booking cancelled.
- Booking rescheduled.

## Financial dashboard (owner only)

All figures are per month, with a month selector.

- **Realized revenue:** confirmed appointments whose time has passed. When
  attendance marking exists, this becomes completed appointments.
- **Forecast revenue:** confirmed appointments still to happen in the month.
- Comparison with the previous month.
- Most booked services, by count and by value.
- Cancellations by reason in a donut chart, with `rescheduled` in a distinct
  color. Rescheduling is shown but excluded from the cancellation rate.
- Summary figures: total appointments, cancellation rate, average ticket.

## Privacy

- Collect only the client data the booking needs.
- No personal data in logs.

## Open questions

- Default language for a visitor who has not chosen one.
- Consent checkbox wording and data retention period.
