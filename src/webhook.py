from fastapi import APIRouter, Request
import os

router = APIRouter()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

@router.get("/webhook")
async def verify_webhook(mode: str = None, challenge: str = None, hub_verify_token: str = None):
    if mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(challenge)
    return {"error": "Invalid verify token"}

@router.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("Incoming WhatsApp Message:", data)
    return {"status": "received"}
