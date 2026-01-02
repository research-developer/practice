"""Tests for the API module."""

import pytest
from practice.api import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestHomeEndpoint:
    """Test cases for home endpoint."""

    def test_home(self, client):
        """Test home endpoint returns expected response."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.get_json()
        assert data["message"] == "Practice API"
        assert data["version"] == "0.1.0"
        assert "timestamp" in data


class TestHealthEndpoint:
    """Test cases for health endpoint."""

    def test_health(self, client):
        """Test health endpoint returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "healthy"
        assert "timestamp" in data


class TestCalculateEndpoint:
    """Test cases for calculate endpoint."""

    def test_calculate_add(self, client):
        """Test calculate endpoint with add operation."""
        response = client.post("/calculate", json={"operation": "add", "a": 5, "b": 3})
        assert response.status_code == 200
        data = response.get_json()
        assert data["result"] == 8
        assert data["operation"] == "add"

    def test_calculate_divide(self, client):
        """Test calculate endpoint with divide operation."""
        response = client.post("/calculate", json={"operation": "divide", "a": 10, "b": 2})
        assert response.status_code == 200
        data = response.get_json()
        assert data["result"] == 5

    def test_calculate_divide_by_zero(self, client):
        """Test calculate endpoint with division by zero."""
        response = client.post("/calculate", json={"operation": "divide", "a": 10, "b": 0})
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data

    def test_calculate_missing_fields(self, client):
        """Test calculate endpoint with missing fields."""
        response = client.post("/calculate", json={"operation": "add", "a": 5})
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data

    def test_calculate_no_json(self, client):
        """Test calculate endpoint without JSON data."""
        response = client.post("/calculate")
        # Flask returns 415 when no Content-Type: application/json is provided
        assert response.status_code in [400, 415]

    def test_calculate_invalid_operation(self, client):
        """Test calculate endpoint with invalid operation."""
        response = client.post("/calculate", json={"operation": "invalid", "a": 5, "b": 3})
        assert response.status_code == 400


class TestOperationsEndpoint:
    """Test cases for operations endpoint."""

    def test_operations(self, client):
        """Test operations endpoint returns list of operations."""
        response = client.get("/operations")
        assert response.status_code == 200
        data = response.get_json()
        assert "operations" in data
        assert isinstance(data["operations"], list)
        assert "add" in data["operations"]
