import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from dotenv import load_dotenv

from src.webhook import router as webhook_router
from src.send_message import router as send_router
from src.config import settings

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
        """Startup and shutdown events."""
        logger.info("WhatsApp Cloud API Starter Kit is starting up...")
        logger.info(f"Graph API version: {settings.GRAPH_API_VERSION}")
        yield
        logger.info("WhatsApp Cloud API Starter Kit is shutting down...")


app = FastAPI(
        title="WhatsApp Cloud API Starter Kit",
        description="A production-ready starter template for WhatsApp Cloud API with FastAPI",
        version="2.0.0",
        lifespan=lifespan,
)

app.include_router(webhook_router, tags=["Webhook"])
app.include_router(send_router, prefix="/api", tags=["Messaging"])


@app.get("/", tags=["Health"])
async def home():
        """Health check endpoint."""
        return {
            "status": "running",
            "service": "WhatsApp Cloud API Starter Kit",
            "version": "2.0.0",
        }


@app.get("/health", tags=["Health"])
async def health_check():
        """Detailed health check endpoint."""
        return {
            "status": "healthy",
            "api_version": settings.GRAPH_API_VERSION,
            "webhook_configured": bool(settings.VERIFY_TOKEN),
            "whatsapp_configured": bool(settings.WHATSAPP_TOKEN and settings.WHATSAPP_PHONE_NUMBER_ID),
        }
