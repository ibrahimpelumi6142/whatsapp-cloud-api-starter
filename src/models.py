from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ---- Request Models ----


class MessageType(str, Enum):
      TEXT = "text"
      IMAGE = "image"
      DOCUMENT = "document"
      TEMPLATE = "template"


class SendTextRequest(BaseModel):
      """Request body for sending a text message."""

    to: str = Field(..., description="Recipient phone number in international format")
    message: str = Field(..., description="Text message body")


class SendImageRequest(BaseModel):
      """Request body for sending an image message."""

    to: str = Field(..., description="Recipient phone number in international format")
    image_url: str = Field(..., alias="image_url", description="Public URL of the image")
    caption: Optional[str] = Field(None, description="Optional image caption")


class SendDocumentRequest(BaseModel):
      """Request body for sending a document message."""

    to: str = Field(..., description="Recipient phone number in international format")
    document_url: str = Field(..., description="Public URL of the document")
    filename: Optional[str] = Field(None, description="Filename to display")
    caption: Optional[str] = Field(None, description="Optional document caption")


class TemplateComponent(BaseModel):
      """Component for template messages."""

    type: str
    parameters: list = Field(default_factory=list)


class SendTemplateRequest(BaseModel):
      """Request body for sending a template message."""

    to: str = Field(..., description="Recipient phone number in international format")
    template_name: str = Field(..., description="Name of the approved message template")
    language_code: str = Field(default="en_US", description="Language code for the template")
    components: list[TemplateComponent] = Field(default_factory=list)


# ---- Response Models ----


class MessageResponse(BaseModel):
      """Standard response for message operations."""

    success: bool
    message_id: Optional[str] = None
    error: Optional[str] = None
