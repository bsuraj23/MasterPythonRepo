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



class ItemRead(ItemCreate):
    id: int
    #adding this for pydantic v2 compatibility
    class Config:
        from_attributes = True  # For Pydantic v2
#       orm_mode = True  # For Pydantic v1
app = FastAPI(title="University Portal API", description="A simple CRUD API with MySQL")



@app.get("/")
def read_root():
    return {"message": "Welcome to University Portal API", "database": "MySQL"}

class ItemCreate(BaseModel):
    name: str
    description: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/", response_model=ItemRead)
def create_item(item: ItemCreate, dbObj: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    #created Item 
    print("Item created ",db_item)
    #send it to DB 

    #confirm


      






    #send it to DB 

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=list[ItemRead])


@app.get("/Items")
def functionWhichWIllExecute():
    #connect to DB
objDB = SessionLocal()
#query to get table data 
objDB.execute("Select* from Items")
objDB.query(Item).all()

objDB.commit()
#close connection
objDB.close()



#


    return Items










def read_items(db: Session = Depends(get_db)):

    
        return db.query(Item).all()

def get_db():
    db = SessionLocal
   return db 



#api
@app.delete("/Items/{item_id}")
def functionAme(itemid: int, db: Session = Depends(get_db)):



    #connect to DB
    db.

   

#commit 
    #close 





#body 







#close 





    return Item









@app.get("/items/{item_id}", response_model=ItemRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    try:
     #query 
    #db.execute("Al")
    except:
    


    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
        raise HTTPException(status_code=403, detail="Item not found")
        #sql erorr 
        #query error


    return db_item

#int, Item
class OwnItemResponse(BaseModel):
    item_id: int
    Item.name: str
    Item.description: str

#api
@app.put("items/{item_id}",response_model=OwnItemResponse)
def fujnciton(item_id:int,body:Item ,db: = Session = Depends(get_db)):
   #connet to DB 
    db= Session = Depends(get_db)
  try:

#query
#sql = 
  db = obj.execute(,
  #query get it 
  db =execute 
  )
#fastAPI Predefined Function 
  db = obj.execute("SELECT * FROM Items WHERE id=:item_id", {"item_id": item_id})





#exception
#commit 
#close 

















#put -- > item id .. connect to DB ... query ... update ... commit ... close

#API
@app.put("/Items/{item_id}")
def update_item(db: Session = Depends(get_db), item_id: int, item: ItemCreate):
     #collect body
     #connect to DB     
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        db_item.name = item.name
        db_item.description = item.description

   db.commit()
   db.close()         




#function ()
  #collect the item number from URL
 
  #connect to DB
  #query to get item    
  #change the values
  #commit
  #save 
  #close


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



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
xyz = FastAPI()
@api.

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}

@app.get("/health")
def function():
    #db check conneectivity
    try:
    db = SessionLocal()
    db.execute(text("SELECT * from items"))
    db.referesh()
    db.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database connection error")
        raise HTTPException(status_code=500, detail="Database connection error")
    return {"message": "Server is healthy", "database": "connected"}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)

    


