"""
Test script to create the hr_management database first
"""
import pymysql

# MySQL connection parameters
MYSQL_PASSWORDS = ["", "root", "pa55worD$#pa", "123456", "admin"]

def create_hr_database():
    """Create the hr_management database if it doesn't exist"""
    
    for password in MYSQL_PASSWORDS:
        try:
            # Connect to MySQL server (without specifying database)
            if password:
                connection = pymysql.connect(
                    host='localhost',
                    user='root',
                    password=password,
                    charset='utf8mb4'
                )
            else:
                connection = pymysql.connect(
                    host='localhost',
                    user='root',
                    charset='utf8mb4'
                )
            
            print(f"✅ Connected to MySQL with {'empty password' if not password else f'password: {password}'}")
            
            # Create database
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS hr_management")
            cursor.execute("SHOW DATABASES LIKE 'hr_management'")
            result = cursor.fetchone()
            
            if result:
                print("✅ Database 'hr_management' created/verified successfully!")
                
                # Test connection to the new database
                cursor.execute("USE hr_management")
                print("✅ Successfully connected to hr_management database!")
                
                cursor.close()
                connection.close()
                return True
            else:
                print("❌ Failed to create database")
                cursor.close()
                connection.close()
                return False
                
        except Exception as e:
            print(f"❌ Failed with password {'(empty)' if not password else password}: {str(e)[:50]}...")
            continue
    
    print("❌ Could not connect to MySQL with any common password.")
    return False

if __name__ == "__main__":
    print("=== Creating hr_management Database ===")
    success = create_hr_database()
    
    if success:
        print("\n🎉 Database setup completed successfully!")
        print("Now you can run: uvicorn main:app --reload --host 127.0.0.1 --port 8001")
    else:
        print("\n❌ Database setup failed. Please check your MySQL configuration.")