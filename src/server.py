from fastapi import FastAPI
from src.webhook import router as webhook_router
from src.send_message import router as send_router

app = FastAPI(title="WhatsApp Cloud API Starter Kit")

app.include_router(webhook_router)
app.include_router(send_router)

@app.get("/")
def home():
    return {"status": "running", "message": "WhatsApp Cloud API Starter Kit"}
