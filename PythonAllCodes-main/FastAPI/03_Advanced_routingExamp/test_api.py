"""
Simple API Testing Script
Tests all endpoints of 03_Advanced_routingExamp
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(name, url, method="GET", **kwargs):
    """Test a single endpoint"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"URL: {url}")
    print(f"{'='*60}")
    
    try:
        if method == "GET":
            response = requests.get(url, **kwargs)
        else:
            response = requests.request(method, url, **kwargs)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response:")
        print(json.dumps(response.json(), indent=2)[:500])  # Limit output
        
        if response.status_code < 400:
            print("✅ PASSED")
            return True
        else:
            print("❌ FAILED")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

print("\n" + "#"*60)
print("# FastAPI Advanced Routing - API Testing")
print("#"*60)

# Test 1: Root endpoint
test_endpoint("Root Endpoint", f"{BASE_URL}/")

# Test 2: Health check
test_endpoint("Health Check", f"{BASE_URL}/health")

# Test 3: Get schemas (with limit)
test_endpoint("Get Schemas (limited)", f"{BASE_URL}/schemas?limit=2")

# Test 4: Get schemas (no limit)
test_endpoint("Get All Schemas", f"{BASE_URL}/schemas")

# Test 5: Get specific schema
test_endpoint("Get Schema by ID", f"{BASE_URL}/schemas/dataset")

# Test 6: Custom API request
test_endpoint(
    "Custom API Request",
    f"{BASE_URL}/api/request?url=https://api.github.com/users/github&timeout=10"
)

# Test 7: Advanced routing
test_endpoint(
    "Advanced Routing",
    f"{BASE_URL}/advanced/5?q=test&skip=0&limit=10"
)

# Test 8: Error handling - invalid item_id
test_endpoint(
    "Error Handling (invalid path param)",
    f"{BASE_URL}/advanced/0"  # Should fail (must be >= 1)
)

# Test 9: Error handling - query too short
test_endpoint(
    "Error Handling (query too short)",
    f"{BASE_URL}/advanced/1?q=ab"  # Should fail (min_length=3)
)

print("\n" + "="*60)
print("✅ All tests completed!")
print("="*60)
print(f"\nAPI Documentation: {BASE_URL}/docs")
print(f"Alternative Docs: {BASE_URL}/redoc")
