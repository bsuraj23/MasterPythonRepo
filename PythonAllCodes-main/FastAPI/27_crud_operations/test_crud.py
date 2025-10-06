import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db, Base, Product

# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test database tables
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Override the dependency
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_database():
    """Clean the database before each test"""
    # Clear all products before each test
    db = TestingSessionLocal()
    db.query(Product).delete()
    db.commit()
    db.close()
    yield
    # Clean up after test
    db = TestingSessionLocal()
    db.query(Product).delete()
    db.commit()
    db.close()

def test_create_product():
    """Test creating a new product"""
    product_data = {
        "name": "Test Product",
        "description": "This is a test product"
    }
    response = client.post("/products/", json=product_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == product_data["name"]
    assert data["description"] == product_data["description"]
    assert "id" in data
    assert isinstance(data["id"], int)

def test_create_product_invalid_data():
    """Test creating a product with invalid data"""
    # Missing required fields
    response = client.post("/products/", json={})
    assert response.status_code == 422
    
    # Invalid data types
    invalid_data = {
        "name": 123,  # Should be string
        "description": "Valid description"
    }
    response = client.post("/products/", json=invalid_data)
    assert response.status_code == 422

def test_read_products_empty():
    """Test reading products when database is empty"""
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []

def test_read_products():
    """Test reading all products"""
    # Create test products
    products = [
        {"name": "Product 1", "description": "Description 1"},
        {"name": "Product 2", "description": "Description 2"}
    ]
    
    created_products = []
    for product in products:
        response = client.post("/products/", json=product)
        created_products.append(response.json())
    
    # Read all products
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    
    # Check that all products are returned
    for i, product in enumerate(data):
        assert product["name"] == products[i]["name"]
        assert product["description"] == products[i]["description"]

def test_read_product_by_id():
    """Test reading a specific product by ID"""
    # Create a product
    product_data = {"name": "Single Product", "description": "Single description"}
    create_response = client.post("/products/", json=product_data)
    created_product = create_response.json()
    
    # Read the product by ID
    response = client.get(f"/products/{created_product['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_product["id"]
    assert data["name"] == product_data["name"]
    assert data["description"] == product_data["description"]

def test_read_product_not_found():
    """Test reading a non-existent product"""
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_update_product():
    """Test updating an existing product"""
    # Create a product
    original_data = {"name": "Original Product", "description": "Original description"}
    create_response = client.post("/products/", json=original_data)
    created_product = create_response.json()
    
    # Update the product
    update_data = {"name": "Updated Product", "description": "Updated description"}
    response = client.put(f"/products/{created_product['id']}", json=update_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_product["id"]
    assert data["name"] == update_data["name"]
    assert data["description"] == update_data["description"]
    
    # Verify the update persisted
    get_response = client.get(f"/products/{created_product['id']}")
    assert get_response.status_code == 200
    get_data = get_response.json()
    assert get_data["name"] == update_data["name"]
    assert get_data["description"] == update_data["description"]

def test_update_product_not_found():
    """Test updating a non-existent product"""
    update_data = {"name": "Updated Product", "description": "Updated description"}
    response = client.put("/products/999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_update_product_invalid_data():
    """Test updating a product with invalid data"""
    # Create a product
    original_data = {"name": "Original Product", "description": "Original description"}
    create_response = client.post("/products/", json=original_data)
    created_product = create_response.json()
    
    # Try to update with invalid data
    invalid_data = {"name": 123, "description": "Valid description"}
    response = client.put(f"/products/{created_product['id']}", json=invalid_data)
    assert response.status_code == 422

def test_delete_product():
    """Test deleting an existing product"""
    # Create a product
    product_data = {"name": "Product to Delete", "description": "Will be deleted"}
    create_response = client.post("/products/", json=product_data)
    created_product = create_response.json()
    
    # Delete the product
    response = client.delete(f"/products/{created_product['id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Product deleted"
    
    # Verify the product is deleted
    get_response = client.get(f"/products/{created_product['id']}")
    assert get_response.status_code == 404

def test_delete_product_not_found():
    """Test deleting a non-existent product"""
    response = client.delete("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_crud_workflow():
    """Test a complete CRUD workflow"""
    # Create
    product_data = {"name": "Workflow Product", "description": "Testing workflow"}
    create_response = client.post("/products/", json=product_data)
    assert create_response.status_code == 200
    created_product = create_response.json()
    
    # Read
    read_response = client.get(f"/products/{created_product['id']}")
    assert read_response.status_code == 200
    
    # Update
    update_data = {"name": "Updated Workflow Product", "description": "Updated workflow"}
    update_response = client.put(f"/products/{created_product['id']}", json=update_data)
    assert update_response.status_code == 200
    
    # Delete
    delete_response = client.delete(f"/products/{created_product['id']}")
    assert delete_response.status_code == 200
    
    # Verify deletion
    final_read = client.get(f"/products/{created_product['id']}")
    assert final_read.status_code == 404

def test_database_persistence():
    """Test that data persists across requests"""
    # Create multiple products
    products = []
    for i in range(3):
        product_data = {"name": f"Product {i}", "description": f"Description {i}"}
        response = client.post("/products/", json=product_data)
        products.append(response.json())
    
    # Read all products multiple times to ensure persistence
    for _ in range(3):
        response = client.get("/products/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3
        
        # Verify all products are still there
        for i, product in enumerate(data):
            assert product["name"] == f"Product {i}"
            assert product["description"] == f"Description {i}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])