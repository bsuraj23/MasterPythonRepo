"""
Comprehensive test suite for FastAPI Testing Demo

This file demonstrates various testing patterns and best practices for FastAPI applications.
Run with: pytest test_main.py -v
"""









import pytest
from fastapi.testclient import TestClient
from main import app, get_database

# Create test client
client = TestClient(app)

# Test database override
test_items_db = []

def override_get_database():
    """Override database dependency for testing"""
    return test_items_db

# Override the dependency
app.dependency_overrides[get_database] = override_get_database

class TestBasicEndpoints:
    """Test basic application endpoints"""
    
    def  funtion(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello, FastAPI testing!"
        assert "version" in data
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "items_count" in data

class TestItemCRUD:
    """Test CRUD operations for items"""
    
    def setup_method(self):
        """Clear test database before each test"""
        test_items_db.clear()
    
    def test_create_item(self):
        """Test item creation"""
        item_data = {
            "name": "Test Item",
            "price": 99.99,
            "description": "A test item",
            "in_stock": True
        }
        response = client.post("/items/", json=item_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["name"] == item_data["name"]
        assert data["price"] == item_data["price"]
        assert data["description"] == item_data["description"]
        assert data["in_stock"] == item_data["in_stock"]
        assert "id" in data
    
    def test_read_items_empty(self):
        """Test reading items when database is empty"""
        response = client.get("/items/")
        assert response.status_code == 200
        assert response.json() == []
    
    def test_read_item_by_id(self):
        """Test reading a specific item by ID"""
        # Create an item
        item_data = {"name": "Specific Item", "price": 50.0}
        create_response = client.post("/items/", json=item_data)
        item_id = create_response.json()["id"]
        
        # Read the item
        response = client.get(f"/items/{item_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == item_data["name"]
        assert data["id"] == item_id
    
    def test_read_nonexistent_item(self):
        """Test reading a non-existent item"""
        response = client.get("/items/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Item not found"
    
    def test_update_item(self):
        """Test updating an existing item"""
        # Create an item
        original_data = {"name": "Original Item", "price": 25.0}
        create_response = client.post("/items/", json=original_data)
        item_id = create_response.json()["id"]
        
        # Update the item
        updated_data = {"name": "Updated Item", "price": 35.0, "description": "Updated description"}
        response = client.put(f"/items/{item_id}", json=updated_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["name"] == updated_data["name"]
        assert data["price"] == updated_data["price"]
        assert data["description"] == updated_data["description"]
        assert data["id"] == item_id
    
    def test_delete_item(self):
        """Test deleting an item"""
        # Create an item
        item_data = {"name": "To Delete", "price": 15.0}
        create_response = client.post("/items/", json=item_data)
        item_id = create_response.json()["id"]
        
        # Delete the item
        response = client.delete(f"/items/{item_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Item deleted successfully"
        
        # Verify it's deleted
        get_response = client.get(f"/items/{item_id}")
        assert get_response.status_code == 404

class TestDataValidation:
    """Test data validation and error handling"""
    
    def test_create_item_invalid_data(self):
        """Test creating item with invalid data"""
        invalid_data = {
            "name": "",  # Empty name
            "price": -10.0  # Negative price might be invalid depending on validation
        }
        response = client.post("/items/", json=invalid_data)
        # FastAPI will return 422 for validation errors
        assert response.status_code == 422

# Homework: Extend tests to cover edge cases, error scenarios, and performance testing