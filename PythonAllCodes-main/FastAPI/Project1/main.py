from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# MySQL database configuration
# Common MySQL passwords to try - update with your actual password
MYSQL_PASSWORDS = ["", "root", "pa55worD$#pa", "123456", "admin"]

def get_database_url():
    """Try different passwords and return working DATABASE_URL"""
    for password in MYSQL_PASSWORDS:
        if password:
            url = f"mysql+pymysql://root:{password}@localhost:3306/university_portal"
        else:
            url = "mysql+pymysql://root@localhost:3306/university_portal"
        
        try:
            # Test connection
            test_engine = create_engine(url)
            test_engine.connect()
            print(f"✅ Connected to MySQL with {'empty password' if not password else f'password: {password}'}")
            return url
        except Exception as e:
            print(f"❌ Failed with password {'(empty)' if not password else password}: {str(e)[:50]}...")
            continue
    
    raise Exception("Could not connect to MySQL with any common password. Please update MYSQL_PASSWORDS list.")

DATABASE_URL = get_database_url()

# Create engine with MySQL-specific settings
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    pool_pre_ping=True,
    pool_recycle=300
)

# Create database if it doesn't exist
def create_database_if_not_exists():
    """Create the university_portal database if it doesn't exist"""
    try:
        # Try to connect to the specific database
        #check if old connection object exists then only 
        engine.connect()
        print("✅ Database 'university_portal' exists and is accessible")
    except Exception as e:
        if "Unknown database" in str(e) or "database doesn't exist" in str(e):
            print("📝 Creating database 'university_portal'...")
            # Connect without database name to create it
            base_url = DATABASE_URL.rsplit('/', 1)[0]  # Remove database name
            temp_engine = create_engine(base_url)
            with temp_engine.connect() as conn:
                conn.execute(text("CREATE DATABASE IF NOT EXISTS university_portal"))
                conn.commit()
            print("✅ Database 'university_portal' created successfully")
        else:
            raise e

create_database_if_not_exists()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), index=True, nullable=False)
    description = Column(String(255), index=True, nullable=True)

# Create tables
Base.metadata.create_all(bind=engine)

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemRead(ItemCreate):
    id: int
    
    class Config:
        from_attributes = True  # For Pydantic v2

app = FastAPI(title="University Portal API", description="A simple CRUD API with MySQL")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to University Portal API", "database": "MySQL"}

@app.post("/itemsmain/", response_model=ItemRead)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=list[ItemRead])
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@app.get("/items/{item_id}", response_model=ItemRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=ItemRead)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}

@app.get("/health")
def health_check():
    """Health check endpoint to verify database connection"""
    try:
        # Test database connection
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


