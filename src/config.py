import os
from dataclasses import dataclass


@dataclass
class Settings:
      """Application settings loaded from environment variables."""

    WHATSAPP_TOKEN: str = os.getenv("WHATSAPP_TOKEN", "")
    WHATSAPP_PHONE_NUMBER_ID: str = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
    WHATSAPP_SECRET: str = os.getenv("WHATSAPP_SECRET", "")
    VERIFY_TOKEN: str = os.getenv("VERIFY_TOKEN", "")
    GRAPH_API_VERSION: str = os.getenv("GRAPH_API_VERSION", "v21.0")

    @property
    def BASE_URL(self) -> str:
              return f"https://graph.facebook.com/{self.GRAPH_API_VERSION}/{self.WHATSAPP_PHONE_NUMBER_ID}"


settings = Settings()
