# 📱 WhatsApp Cloud API Starter Kit (FastAPI) v2.0

A production-ready starter template for building WhatsApp automation, bots, and integrations using the **Meta WhatsApp Cloud API** and **Python FastAPI**.

[![CI](https://github.com/ibrahimpelumi6142/whatsapp-cloud-api-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/ibrahimpelumi6142/whatsapp-cloud-api-starter/actions/workflows/ci.yml)

Perfect for:
- Developers building WhatsApp bots
- Automation workflows
- Webhook receivers
- Message notifications
- Learning the Cloud API basics

---

## 🚀 Features

- Receive messages via secure webhook (HMAC SHA-256 signature verification)
- Send text messages
- Send images, documents, templates
- Async HTTP with httpx (non-blocking)
- Pydantic request/response validation
- Configurable Graph API version
- Health check endpoints
- `.env` environment setup
- Docker and docker-compose support
- CI/CD with GitHub Actions
- Tests with pytest
- Proper logging and error handling

---

## 📁 Project Structure

```txt
whatsapp-cloud-api-starter/
 ├─ src/
 │  ├─ __init__.py
 │  ├─ server.py            # FastAPI server with lifespan
 │  ├─ config.py            # Centralized settings
 │  ├─ models.py            # Pydantic request/response models
 │  ├─ send_message.py      # Messaging endpoints
 │  ├─ webhook.py           # Webhook handler
 │  └─ utils/
 │     ├─ __init__.py
 │     └─ verify_signature.py
 ├─ tests/
 │  └─ test_endpoints.py
 ├─ examples/
 │  └─ sample_payload.json
 ├─ .github/workflows/ci.yml
 ├─ .env.example
 ├─ .gitignore
 ├─ Dockerfile
 ├─ docker-compose.yml
 ├─ requirements.txt
 ├─ README.md
 └─ LICENSE
```

---

## 🔧 Installation

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

### Create .env file:

```bash
cp .env.example .env
```

```
WHATSAPP_TOKEN=your_api_token
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
WHATSAPP_SECRET=your_app_secret
VERIFY_TOKEN=your_webhook_verify_token
GRAPH_API_VERSION=v21.0
```

---

## 🚀 Running Locally

```bash
uvicorn src.server:app --reload
```

Your server runs at: `http://localhost:8000`

Interactive API docs at: `http://localhost:8000/docs`

---

## 🐳 Docker

```bash
docker compose up --build
```

---

## 🔗 Webhook Verification

Meta will call:

```
GET /webhook?hub.verify_token=xxx&hub.challenge=yyy
```

We return the challenge if tokens match.

---

## 📩 Sending Messages

All messaging endpoints are under the `/api` prefix.

### Send a text message

```
POST /api/send-message
```

```json
{
  "to": "2348012345678",
  "message": "Hello from WhatsApp Cloud API Starter Kit!"
}
```

### Send an image

```
POST /api/send-image
```

```json
{
  "to": "2348012345678",
  "image_url": "https://example.com/photo.jpg",
  "caption": "Check this out"
}
```

### Send a document

```
POST /api/send-document
```

```json
{
  "to": "2348012345678",
  "document_url": "https://example.com/file.pdf",
  "filename": "report.pdf"
}
```

### Send a template message

```
POST /api/send-template
```

```json
{
  "to": "2348012345678",
  "template_name": "hello_world",
  "language_code": "en_US"
}
```

---

## 📥 Receiving Messages

WhatsApp will POST incoming messages to:

```
POST /webhook
```

Incoming payloads are validated with HMAC SHA-256 signature verification.

---

## 🧪 Testing

```bash
pytest tests/ -v
```

---

## 📝 License

MIT License
Free to use, modify, and distribute.

---

## 👨‍💻 Author

- Lasisi Ibrahim Pelumi
- Full-Stack Engineer • WhatsApp Automation Expert
- GitHub: https://github.com/ibrahimpelumi6142
