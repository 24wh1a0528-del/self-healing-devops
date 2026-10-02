"""
Unit Tests for the Self-Healing DevOps Platform Flask Application
Phase 1: Testing the home page and health check endpoint
"""

import json
import pytest
from app import app as flask_app


# ──────────────────────────────────────────────
# Fixtures
# A "fixture" is reusable setup code that pytest
# runs automatically before each test function.
# ──────────────────────────────────────────────

@pytest.fixture
def app():
    """Create a test version of the Flask app."""
    flask_app.config["TESTING"] = True   # Enables test mode (better error messages)
    flask_app.config["DEBUG"] = False
    yield flask_app


@pytest.fixture
def client(app):
    """Create a test client that can send fake HTTP requests to the app."""
    return app.test_client()


# ──────────────────────────────────────────────
# Tests for the Home Page  GET /
# ──────────────────────────────────────────────

class TestHomePage:
    """Tests for the home page route."""

    def test_home_page_returns_200(self, client):
        """The home page should respond with HTTP 200 (OK)."""
        response = client.get("/")
        assert response.status_code == 200, (
            f"Expected status 200 but got {response.status_code}"
        )

    def test_home_page_contains_app_name(self, client):
        """The home page HTML should contain the application name."""
        response = client.get("/")
        html = response.data.decode("utf-8")
        assert "Self-Healing DevOps Platform" in html, (
            "App name not found in home page HTML"
        )

    def test_home_page_contains_version(self, client):
        """The home page HTML should contain the version number."""
        response = client.get("/")
        html = response.data.decode("utf-8")
        assert "1.0.0" in html, (
            "Version number not found in home page HTML"
        )

    def test_home_page_content_type_is_html(self, client):
        """The home page should return HTML content."""
        response = client.get("/")
        assert "text/html" in response.content_type, (
            f"Expected HTML content type but got {response.content_type}"
        )


# ──────────────────────────────────────────────
# Tests for the Health Endpoint  GET /health
# ──────────────────────────────────────────────

class TestHealthEndpoint:
    """Tests for the /health route."""

    def test_health_returns_200(self, client):
        """The /health endpoint should respond with HTTP 200 (OK)."""
        response = client.get("/health")
        assert response.status_code == 200, (
            f"Expected status 200 but got {response.status_code}"
        )

    def test_health_returns_json(self, client):
        """The /health endpoint should return JSON content."""
        response = client.get("/health")
        assert "application/json" in response.content_type, (
            f"Expected JSON content type but got {response.content_type}"
        )

    def test_health_status_is_healthy(self, client):
        """The /health endpoint JSON body must contain status: healthy."""
        response = client.get("/health")
        data = json.loads(response.data)
        assert "status" in data, "Response JSON missing 'status' key"
        assert data["status"] == "healthy", (
            f"Expected 'healthy' but got '{data['status']}'"
        )

    def test_health_response_has_no_extra_keys(self, client):
        """The /health response should only contain the 'status' key."""
        response = client.get("/health")
        data = json.loads(response.data)
        assert list(data.keys()) == ["status"], (
            f"Expected only ['status'] key but found {list(data.keys())}"
        )


# ──────────────────────────────────────────────
# Tests for invalid routes
# ──────────────────────────────────────────────

class TestInvalidRoutes:
    """Tests for routes that do not exist."""

    def test_unknown_route_returns_404(self, client):
        """Requesting a non-existent route should return HTTP 404 (Not Found)."""
        response = client.get("/does-not-exist")
        assert response.status_code == 404, (
            f"Expected 404 but got {response.status_code}"
        )
