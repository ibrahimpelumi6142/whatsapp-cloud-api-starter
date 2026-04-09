import os
import pytest
from fastapi.testclient import TestClient

os.environ["WHATSAPP_TOKEN"] = "test_token"
os.environ["WHATSAPP_PHONE_NUMBER_ID"] = "123456789"
os.environ["WHATSAPP_SECRET"] = "test_secret"
os.environ["VERIFY_TOKEN"] = "test_verify_token"

from src.server import app

client = TestClient(app)


class TestHealthEndpoints:
      def test_home(self):
                response = client.get("/")
                assert response.status_code == 200
                data = response.json()
                assert data["status"] == "running"

      def test_health_check(self):
                response = client.get("/health")
                assert response.status_code == 200
                data = response.json()
                assert data["status"] == "healthy"


class TestWebhookVerification:
      def test_valid_verification(self):
                response = client.get(
                              "/webhook",
                              params={"hub.mode": "subscribe", "hub.challenge": "12345", "hub.verify_token": "test_verify_token"},
                )
                assert response.status_code == 200
                assert response.json() == 12345

      def test_invalid_token(self):
                response = client.get(
                              "/webhook",
                              params={"hub.mode": "subscribe", "hub.challenge": "12345", "hub.verify_token": "wrong_token"},
                )
                assert response.status_code == 403

      def test_missing_params(self):
                response = client.get("/webhook")
                assert response.status_code == 403
