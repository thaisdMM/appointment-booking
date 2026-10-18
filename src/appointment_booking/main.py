from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health() -> dict[str, str]:
    """Report that the application is up."""
    return {"status": "ok"}
