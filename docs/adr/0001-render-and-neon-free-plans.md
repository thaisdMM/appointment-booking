# Render and Neon free plans for deployment

The app runs on Render and the PostgreSQL database on Neon, both on their free
plans and in the Frankfurt region, the closest to the clinic in Zurich. Being a
portfolio project, it accepts the free plans' limits instead of paying: the
Render service spins down after 15 minutes without traffic and takes about a
minute to wake up, and it has no pre-deploy command, so database migrations run
when the container starts. Render deploys `main` only after the CI checks pass.

## Considered Options

- Render paid plan: always awake and with a pre-deploy command, rejected for
  its monthly cost.
