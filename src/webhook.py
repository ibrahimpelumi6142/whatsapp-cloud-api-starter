import logging
from typing import Optional

from fastapi import APIRouter, Header, HTTPException, Query, Request

from src.config import settings
from src.utils.verify_signature import verify_webhook_signature

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/webhook")
async def verify_webhook(
        hub_mode: Optional[str] = Query(None, alias="hub.mode"),
        hub_challenge: Optional[str] = Query(None, alias="hub.challenge"),
        hub_verify_token: Optional[str] = Query(None, alias="hub.verify_token"),
):
        """
            Webhook verification endpoint.

                Meta sends a GET request with hub.mode, hub.challenge, and hub.verify_token
                    to verify the webhook URL during setup.
                        """
        if hub_mode == "subscribe" and hub_verify_token == settings.VERIFY_TOKEN:
                    logger.info("Webhook verified successfully")
                    return int(hub_challenge)

        logger.warning(f"Webhook verification failed: mode={hub_mode}")
        raise HTTPException(status_code=403, detail="Verification failed")


@router.post("/webhook")
async def receive_message(
        request: Request,
        x_hub_signature_256: Optional[str] = Header(None, alias="X-Hub-Signature-256"),
):
        """
            Receive incoming WhatsApp messages.

                Validates the request signature using HMAC SHA-256 before processing.
                    """
        body = await request.body()

    # Verify webhook signature
        if not verify_webhook_signature(body, x_hub_signature_256):
                    logger.error("Invalid webhook signature — rejecting request")
                    raise HTTPException(status_code=401, detail="Invalid signature")

        data = await request.json()

    # Extract messages from the webhook payload
        try:
                    entries = data.get("entry", [])
                    for entry in entries:
                                    changes = entry.get("changes", [])
                                    for change in changes:
                                                        value = change.get("value", {})
                                                        messages = value.get("messages", [])
                                                        for message in messages:
                                                                                sender = message.get("from", "unknown")
                                                                                msg_type = message.get("type", "unknown")

                                                            if msg_type == "text":
                                                                                        text_body = message.get("text", {}).get("body", "")
                                                                                        logger.info(f"Text message from {sender}: {text_body}")
        else:
                                    logger.info(f"{msg_type} message from {sender}")

                    # Handle message statuses (delivered, read, etc.)
                            statuses = value.get("statuses", [])
                for status in statuses:
                                        logger.info(
                                                                    f"Message {status.get('id')} status: {status.get('status')}"
                                        )
except Exception as e:
        logger.error(f"Error processing webhook payload: {e}")

    return {"status": "received"}
