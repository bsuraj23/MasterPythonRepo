#!/usr/bin/env python3
"""
End-to-end test script for FastAPI Database Integration

This script tests all API endpoints to ensure the application is working correctly.
"""

import requests
import json
import sys
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_root_endpoint():
    """Test the root endpoint"""
    print("\nTesting root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Root endpoint passed")
            data = response.json()
            print(f"   Title: {data.get('title', 'N/A')}")
            print(f"   Features: {len(data.get('features', []))} features")
            return True
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
        return False

def test_create_item():
    """Test creating a new item"""
    print("\nTesting item creation...")
    test_item = {
        "name": "Test Laptop",
        "description": "A high-performance laptop for testing",
        "price": "1299.99",
        "category": "electronics",
        "is_active": True
    }
    
    try:
        response = requests.post(f"{BASE_URL}/items/", json=test_item)
        if response.status_code == 201:
            print("✅ Item creation passed")
            data = response.json()
            print(f"   Created item ID: {data['id']}")
            print(f"   Name: {data['name']}")
            return data['id']
        else:
            print(f"❌ Item creation failed: {response.status_code}")
            if response.text:
                print(f"   Error: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Item creation error: {e}")
        return None

def test_get_item(item_id):
    """Test retrieving a specific item"""
    print(f"\nTesting get item {item_id}...")
    try:
        response = requests.get(f"{BASE_URL}/items/{item_id}")
        if response.status_code == 200:
            print("✅ Get item passed")
            data = response.json()
            print(f"   Item: {data['name']} - ${data.get('price', 'N/A')}")
            return True
        else:
            print(f"❌ Get item failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Get item error: {e}")
        return False

def test_get_items():
    """Test retrieving all items"""
    print("\nTesting get all items...")
    try:
        response = requests.get(f"{BASE_URL}/items/")
        if response.status_code == 200:
            print("✅ Get items passed")
            data = response.json()
            print(f"   Total items: {data['total']}")
            print(f"   Items on page: {len(data['items'])}")
            return True
        else:
            print(f"❌ Get items failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Get items error: {e}")
        return False

def test_update_item(item_id):
    """Test updating an item"""
    print(f"\nTesting update item {item_id}...")
    update_data = {
        "price": "1199.99",
        "description": "Updated description - now on sale!"
    }
    
    try:
        response = requests.put(f"{BASE_URL}/items/{item_id}", json=update_data)
        if response.status_code == 200:
            print("✅ Update item passed")
            data = response.json()
            print(f"   Updated price: ${data['price']}")
            return True
        else:
            print(f"❌ Update item failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Update item error: {e}")
        return False

def test_search_items():
    """Test searching items"""
    print("\nTesting search functionality...")
    try:
        response = requests.get(f"{BASE_URL}/items/?search=laptop")
        if response.status_code == 200:
            print("✅ Search items passed")
            data = response.json()
            print(f"   Found {data['total']} items with 'laptop'")
            return True
        else:
            print(f"❌ Search items failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Search items error: {e}")
        return False

def test_filter_items():
    """Test filtering items by category"""
    print("\nTesting filter by category...")
    try:
        response = requests.get(f"{BASE_URL}/items/?category=electronics")
        if response.status_code == 200:
            print("✅ Filter items passed")
            data = response.json()
            print(f"   Found {data['total']} electronics items")
            return True
        else:
            print(f"❌ Filter items failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Filter items error: {e}")
        return False

def test_statistics():
    """Test statistics endpoint"""
    print("\nTesting statistics...")
    try:
        response = requests.get(f"{BASE_URL}/stats")
        if response.status_code == 200:
            print("✅ Statistics passed")
            data = response.json()
            print(f"   Total items: {data['total_items']}")
            print(f"   Active items: {data['active_items']}")
            print(f"   Database type: {data['database_type']}")
            return True
        else:
            print(f"❌ Statistics failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Statistics error: {e}")
        return False

def test_categories():
    """Test categories endpoint"""
    print("\nTesting categories...")
    try:
        response = requests.get(f"{BASE_URL}/categories")
        if response.status_code == 200:
            print("✅ Categories passed")
            data = response.json()
            print(f"   Categories: {data['categories']}")
            return True
        else:
            print(f"❌ Categories failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Categories error: {e}")
        return False

def test_soft_delete(item_id):
    """Test soft deleting an item"""
    print(f"\nTesting soft delete item {item_id}...")
    try:
        response = requests.delete(f"{BASE_URL}/items/{item_id}")
        if response.status_code == 200:
            print("✅ Soft delete passed")
            data = response.json()
            print(f"   Message: {data['message']}")
            return True
        else:
            print(f"❌ Soft delete failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Soft delete error: {e}")
        return False

def run_all_tests():
    """Run all tests in sequence"""
    print("🚀 Starting FastAPI Database Integration Tests")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Health check
    total_tests += 1
    if test_health_check():
        tests_passed += 1
    
    # Test 2: Root endpoint
    total_tests += 1
    if test_root_endpoint():
        tests_passed += 1
    
    # Test 3: Statistics (before creating items)
    total_tests += 1
    if test_statistics():
        tests_passed += 1
    
    # Test 4: Create item
    total_tests += 1
    item_id = test_create_item()
    if item_id:
        tests_passed += 1
        
        # Test 5: Get specific item
        total_tests += 1
        if test_get_item(item_id):
            tests_passed += 1
        
        # Test 6: Update item
        total_tests += 1
        if test_update_item(item_id):
            tests_passed += 1
        
        # Test 7: Soft delete item
        total_tests += 1
        if test_soft_delete(item_id):
            tests_passed += 1
    else:
        total_tests += 3  # Skip dependent tests
    
    # Test 8: Get all items
    total_tests += 1
    if test_get_items():
        tests_passed += 1
    
    # Test 9: Search items
    total_tests += 1
    if test_search_items():
        tests_passed += 1
    
    # Test 10: Filter items
    total_tests += 1
    if test_filter_items():
        tests_passed += 1
    
    # Test 11: Categories
    total_tests += 1
    if test_categories():
        tests_passed += 1
    
    # Test 12: Statistics (after operations)
    total_tests += 1
    if test_statistics():
        tests_passed += 1
    
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS")
    print("=" * 50)
    print(f"✅ Tests passed: {tests_passed}")
    print(f"❌ Tests failed: {total_tests - tests_passed}")
    print(f"📈 Success rate: {(tests_passed/total_tests)*100:.1f}%")
    
    if tests_passed == total_tests:
        print("\n🎉 ALL TESTS PASSED! The API is working correctly.")
        return True
    else:
        print(f"\n⚠️  {total_tests - tests_passed} test(s) failed. Please check the server and try again.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)