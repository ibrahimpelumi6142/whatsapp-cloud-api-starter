from fastapi import APIRouter
import requests, os

router = APIRouter()

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")

@router.post("/send-message")
async def send_message(payload: dict):
    url = f"https://graph.facebook.com/v18.0/{PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": payload["to"],
        "type": "text",
        "text": {"body": payload["message"]}
    }

    r = requests.post(url, headers=headers, json=data)
    return r.json()
