"""
End-to-End API Testing Script for Project3
Tests all CRUD operations
"""

import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000"

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def test_root():
    """Test root endpoint"""
    print_section("TEST 1: Root Endpoint")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    print("✅ Root endpoint test PASSED")

def test_health():
    """Test health check endpoint"""
    print_section("TEST 2: Health Check")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✅ Health check test PASSED")

def test_create_items():
    """Test creating multiple items"""
    print_section("TEST 3: Create Items (POST)")
    
    items_to_create = [
        {"name": "Laptop", "description": "Dell XPS 15 Gaming Laptop"},
        {"name": "Mouse", "description": "Logitech Wireless Mouse"},
        {"name": "Keyboard", "description": "Mechanical RGB Keyboard"},
        {"name": "Monitor", "description": "27-inch 4K Display"}
    ]
    
    created_items = []
    for item in items_to_create:
        response = requests.post(f"{BASE_URL}/items/", json=item)
        print(f"\nCreating: {item['name']}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        assert response.status_code == 200
        created_items.append(response.json())
    
    print(f"\n✅ Created {len(created_items)} items successfully")
    return created_items

def test_get_all_items():
    """Test retrieving all items"""
    print_section("TEST 4: Get All Items (GET)")
    response = requests.get(f"{BASE_URL}/items/")
    print(f"Status Code: {response.status_code}")
    items = response.json()
    print(f"Total Items: {len(items)}")
    print(f"Response: {json.dumps(items, indent=2)}")
    assert response.status_code == 200
    assert len(items) > 0
    print("✅ Get all items test PASSED")
    return items

def test_get_single_item(item_id):
    """Test retrieving a single item by ID"""
    print_section(f"TEST 5: Get Single Item (GET /items/{item_id})")
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id
    print("✅ Get single item test PASSED")

def test_update_item(item_id):
    """Test updating an item"""
    print_section(f"TEST 6: Update Item (PUT /items/{item_id})")
    updated_data = {
        "name": "Updated Laptop",
        "description": "Dell XPS 15 - UPDATED with 32GB RAM"
    }
    response = requests.put(f"{BASE_URL}/items/{item_id}", json=updated_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]
    print("✅ Update item test PASSED")

def test_delete_item(item_id):
    """Test deleting an item"""
    print_section(f"TEST 7: Delete Item (DELETE /items/{item_id})")
    response = requests.delete(f"{BASE_URL}/items/{item_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    
    # Verify item is deleted
    verify_response = requests.get(f"{BASE_URL}/items/{item_id}")
    print(f"\nVerifying deletion...")
    print(f"Status Code: {verify_response.status_code}")
    assert verify_response.status_code == 404
    print("✅ Delete item test PASSED")

def test_get_nonexistent_item():
    """Test getting an item that doesn't exist"""
    print_section("TEST 8: Get Non-Existent Item (Error Handling)")
    response = requests.get(f"{BASE_URL}/items/99999")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
    print("✅ Error handling test PASSED")

def test_update_nonexistent_item():
    """Test updating an item that doesn't exist"""
    print_section("TEST 9: Update Non-Existent Item (Error Handling)")
    updated_data = {"name": "Test", "description": "Test"}
    response = requests.put(f"{BASE_URL}/items/99999", json=updated_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 404
    print("✅ Update non-existent item test PASSED")

def test_delete_nonexistent_item():
    """Test deleting an item that doesn't exist"""
    print_section("TEST 10: Delete Non-Existent Item (Error Handling)")
    response = requests.delete(f"{BASE_URL}/items/99999")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 404
    print("✅ Delete non-existent item test PASSED")

def run_all_tests():
    """Run all tests in sequence"""
    print("\n" + "#" * 60)
    print("#  University Portal API - End-to-End Testing")
    print("#" * 60)
    
    try:
        # Wait for server to be ready
        print("\nWaiting for server to be ready...")
        time.sleep(2)
        
        # Run tests
        test_root()
        test_health()
        created_items = test_create_items()
        all_items = test_get_all_items()
        
        if all_items:
            first_item_id = all_items[0]["id"]
            test_get_single_item(first_item_id)
            test_update_item(first_item_id)
            test_delete_item(first_item_id)
        
        test_get_nonexistent_item()
        test_update_nonexistent_item()
        test_delete_nonexistent_item()
        
        # Final summary
        print("\n" + "=" * 60)
        print("  🎉 ALL TESTS PASSED SUCCESSFULLY! 🎉")
        print("=" * 60)
        print(f"\nTotal Tests Run: 10")
        print(f"✅ Passed: 10")
        print(f"❌ Failed: 0")
        
        # Show final state
        print("\n" + "=" * 60)
        print("  Final Database State")
        print("=" * 60)
        final_items = requests.get(f"{BASE_URL}/items/").json()
        print(f"Total items in database: {len(final_items)}")
        for item in final_items:
            print(f"  - {item['id']}: {item['name']}")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Could not connect to server!")
        print(f"Make sure the server is running on {BASE_URL}")
        print("Start server with: uvicorn main:app --reload --port 8003")
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    run_all_tests()
