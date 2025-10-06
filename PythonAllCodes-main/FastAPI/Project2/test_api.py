"""
Manual API Test for Project2 HR Management System
This script tests the API by making HTTP requests
"""

import requests
import json
import time

# Server configuration
BASE_URL = "http://127.0.0.1:8001"

def test_server_connection():
    """Test if the server is running"""
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running!")
            return True
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running or connection failed")
        return False
    except Exception as e:
        print(f"❌ Error connecting to server: {e}")
        return False

def test_health_endpoint():
    """Test the health check endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"🏥 Health Check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Status: {data.get('status')}")
            print(f"   Database: {data.get('database')}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_organizations():
    """Test Organization CRUD operations"""
    print("\n🏢 TESTING ORGANIZATION CRUD OPERATIONS")
    
    # 1. Create Organization
    org_data = {
        "name": "Tech Corp",
        "email": "info@techcorp.com",
        "description": "A leading technology company",
        "phone": "+1-555-0123",
        "address": "123 Tech Street, Silicon Valley, CA",
        "website": "https://techcorp.com",
        "founded_year": 2010
    }
    
    try:
        response = requests.post(f"{BASE_URL}/organizations/", json=org_data)
        print(f"📝 Create Organization: {response.status_code}")
        if response.status_code == 200:
            org = response.json()
            org_id = org['id']
            print(f"   Created organization ID: {org_id}")
            
            # 2. Read Organization
            response = requests.get(f"{BASE_URL}/organizations/{org_id}")
            print(f"📖 Read Organization: {response.status_code}")
            
            # 3. List Organizations
            response = requests.get(f"{BASE_URL}/organizations/")
            print(f"📋 List Organizations: {response.status_code}")
            if response.status_code == 200:
                orgs = response.json()
                print(f"   Found {len(orgs)} organizations")
            
            # 4. Update Organization
            update_data = {"description": "Updated: A leading technology company"}
            response = requests.put(f"{BASE_URL}/organizations/{org_id}", json=update_data)
            print(f"✏️ Update Organization: {response.status_code}")
            
            return org_id
            
    except Exception as e:
        print(f"❌ Organization tests failed: {e}")
        return None

def test_departments(org_id):
    """Test Department CRUD operations"""
    print("\n🏛️ TESTING DEPARTMENT CRUD OPERATIONS")
    
    if not org_id:
        print("❌ No organization ID provided")
        return None
    
    # 1. Create Department
    dept_data = {
        "name": "Engineering",
        "description": "Software development and engineering",
        "budget": 500000.00,
        "organization_id": org_id
    }
    
    try:
        response = requests.post(f"{BASE_URL}/departments/", json=dept_data)
        print(f"📝 Create Department: {response.status_code}")
        if response.status_code == 200:
            dept = response.json()
            dept_id = dept['id']
            print(f"   Created department ID: {dept_id}")
            
            # 2. Read Department
            response = requests.get(f"{BASE_URL}/departments/{dept_id}")
            print(f"📖 Read Department: {response.status_code}")
            
            # 3. List Departments
            response = requests.get(f"{BASE_URL}/departments/")
            print(f"📋 List Departments: {response.status_code}")
            
            # 4. List Departments by Organization
            response = requests.get(f"{BASE_URL}/organizations/{org_id}/departments")
            print(f"🏢 Organization Departments: {response.status_code}")
            
            return dept_id
            
    except Exception as e:
        print(f"❌ Department tests failed: {e}")
        return None

def test_employees(dept_id):
    """Test Employee CRUD operations"""
    print("\n👥 TESTING EMPLOYEE CRUD OPERATIONS")
    
    if not dept_id:
        print("❌ No department ID provided")
        return None
    
    # 1. Create Employee
    emp_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@techcorp.com",
        "phone": "+1-555-0124",
        "position": "Senior Software Engineer",
        "salary": 90000.00,
        "department_id": dept_id
    }
    
    try:
        response = requests.post(f"{BASE_URL}/employees/", json=emp_data)
        print(f"📝 Create Employee: {response.status_code}")
        if response.status_code == 200:
            emp = response.json()
            emp_id = emp['id']
            print(f"   Created employee ID: {emp_id}")
            
            # 2. Read Employee
            response = requests.get(f"{BASE_URL}/employees/{emp_id}")
            print(f"📖 Read Employee: {response.status_code}")
            
            # 3. List Employees
            response = requests.get(f"{BASE_URL}/employees/")
            print(f"📋 List Employees: {response.status_code}")
            
            # 4. List Employees by Department
            response = requests.get(f"{BASE_URL}/departments/{dept_id}/employees")
            print(f"🏛️ Department Employees: {response.status_code}")
            
            return emp_id
            
    except Exception as e:
        print(f"❌ Employee tests failed: {e}")
        return None

def test_analytics():
    """Test Analytics endpoint"""
    print("\n📊 TESTING ANALYTICS")
    
    try:
        response = requests.get(f"{BASE_URL}/analytics/summary")
        print(f"📈 Analytics Summary: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Organizations: {data.get('organizations')}")
            print(f"   Departments: {data.get('departments')}")
            print(f"   Employees: {data.get('employees')}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Analytics test failed: {e}")
        return False

def main():
    """Run all API tests"""
    print("🧪 STARTING PROJECT2 HR MANAGEMENT SYSTEM API TESTS")
    print("=" * 60)
    
    # Check if server is running
    if not test_server_connection():
        print("\n❌ Please start the server first:")
        print("   cd Project2")
        print("   .\venv\Scripts\Activate.ps1")
        print("   python main.py")
        return
    
    # Test health endpoint
    test_health_endpoint()
    
    # Test CRUD operations
    org_id = test_organizations()
    dept_id = test_departments(org_id) if org_id else None
    emp_id = test_employees(dept_id) if dept_id else None
    
    # Test analytics
    test_analytics()
    
    print("\n" + "=" * 60)
    print("🎉 API TESTS COMPLETED!")
    print(f"📊 Visit API docs: {BASE_URL}/docs")

if __name__ == "__main__":
    main()