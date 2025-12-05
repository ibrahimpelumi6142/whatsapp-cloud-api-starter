# 📱 WhatsApp Cloud API Starter Kit (FastAPI)

A simple and clean starter template for building WhatsApp automation, bots, and integrations using the **Meta WhatsApp Cloud API** and **Python FastAPI**.

Perfect for:
- Developers building WhatsApp bots
- Automation workflows
- Webhook receivers
- Message notifications
- Learning the Cloud API basics

---

## 🚀 Features

- Receive messages via webhook  
- Send text messages  
- Send images, documents, templates  
- Verify webhook token  
- Clean folder structure  
- `.env` environment setup  
- Works on localhost or production  
- Easy to deploy  

---

## 📁 Project Structure

```txt
whatsapp-cloud-api-starter/
 ├─ src/
 │   ├─ server.py              # FastAPI server
 │   ├─ send_message.py        # Send message function
 │   ├─ webhook.py             # Webhook handler
 │   └─ utils/
 │        └─ verify_signature.py
 ├─ examples/
 │   └─ sample_payload.json
 ├─ .env.example
 ├─ requirements.txt
 ├─ README.md
 └─ LICENSE

```

---

## 🔧 Installation

```txt
pip install -r requirements.txt

```
---

## ⚙️ Environment Variables

### Create .env file:

```txt
WHATSAPP_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_SECRET=
VERIFY_TOKEN=your_webhook_verify_token

```
---

## 🚀 Running Locally

```txt
uvicorn src.server:app --reload

```
---

## Your server runs at:

```txt
http://localhost:8000

```
---

## 🔗 Webhook Verification

### Meta will call:

```txt
GET /webhook?hub.verify_token=xxx&hub.challenge=yyy

```

### We return the challenge if tokens match.

## 📩 Sending a WhatsApp Message

```txt
POST http://localhost:8000/send-message

```

### JSON:

```txt
{
  "to": "2348012345678",
  "message": "Hello from WhatsApp Cloud API Starter Kit!"
}

```

---

## 📥 Receiving Messages

### WhatsApp will POST incoming messages to:

```txt
POST /webhook

```

### You will receive a structure like:

```txt
{
  "entry": [
    {
      "changes": [
        {
          "value": {
            "messages": [
              {
                "from": "2348012345678",
                "text": { "body": "Hello" }
              }
            ]
          }
        }
      ]
    }
  ]
}

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
