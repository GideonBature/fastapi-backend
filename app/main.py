from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(title="User Management API")

app.include_router(api_router)

@app.get("/")
async def health():
    return { "status": "ok" }