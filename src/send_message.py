import logging

import httpx
from fastapi import APIRouter, HTTPException

from src.config import settings
from src.models import (
    MessageResponse,
    SendDocumentRequest,
    SendImageRequest,
    SendTemplateRequest,
    SendTextRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter()


async def _send_whatsapp_message(payload: dict) -> MessageResponse:
        """
            Send a message via the WhatsApp Cloud API using httpx (async).

                Args:
                        payload: The WhatsApp API message payload.

                            Returns:
                                    MessageResponse with success status and message ID.
                                        """
        url = f"{settings.BASE_URL}/messages"
        headers = {
            "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
            "Content-Type": "application/json",
        }

    async with httpx.AsyncClient(timeout=30.0) as client:
                try:
                                response = await client.post(url, headers=headers, json=payload)
                                data = response.json()

                    if response.status_code == 200:
                                        message_id = data.get("messages", [{}])[0].get("id", "")
                                        logger.info(f"Message sent successfully: {message_id}")
                                        return MessageResponse(success=True, message_id=message_id)

            error_msg = data.get("error", {}).get("message", "Unknown error")
            logger.error(f"WhatsApp API error: {error_msg}")
            return MessageResponse(success=False, error=error_msg)

except httpx.TimeoutException:
            logger.error("WhatsApp API request timed out")
            return MessageResponse(success=False, error="Request timed out")
except httpx.RequestError as e:
            logger.error(f"Request error: {e}")
            return MessageResponse(success=False, error=str(e))


@router.post("/send-message", response_model=MessageResponse)
async def send_text_message(payload: SendTextRequest):
        """Send a text message to a WhatsApp number."""
    data = {
                "messaging_product": "whatsapp",
                "to": payload.to,
                "type": "text",
                "text": {"body": payload.message},
    }
    return await _send_whatsapp_message(data)


@router.post("/send-image", response_model=MessageResponse)
async def send_image_message(payload: SendImageRequest):
        """Send an image message to a WhatsApp number."""
    image_data = {"link": payload.image_url}
    if payload.caption:
                image_data["caption"] = payload.caption

    data = {
                "messaging_product": "whatsapp",
                "to": payload.to,
                "type": "image",
                "image": image_data,
    }
    return await _send_whatsapp_message(data)


@router.post("/send-document", response_model=MessageResponse)
async def send_document_message(payload: SendDocumentRequest):
        """Send a document message to a WhatsApp number."""
    doc_data = {"link": payload.document_url}
    if payload.filename:
                doc_data["filename"] = payload.filename
    if payload.caption:
                doc_data["caption"] = payload.caption

    data = {
                "messaging_product": "whatsapp",
                "to": payload.to,
                "type": "document",
                "document": doc_data,
    }
    return await _send_whatsapp_message(data)


@router.post("/send-template", response_model=MessageResponse)
async def send_template_message(payload: SendTemplateRequest):
        """Send a template message to a WhatsApp number."""
    template_data = {
                "name": payload.template_name,
                "language": {"code": payload.language_code},
    }
    if payload.components:
                template_data["components"] = [c.model_dump() for c in payload.components]

    data = {
                "messaging_product": "whatsapp",
                "to": payload.to,
                "type": "template",
                "template": template_data,
    }
    return await _send_whatsapp_message(data)
