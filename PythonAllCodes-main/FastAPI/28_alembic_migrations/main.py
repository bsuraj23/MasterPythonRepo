from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./alembic_demo.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Tables are created by Alembic migrations, not here!
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Alembic migrations demo"}

    #Homework: Create Alembic migration scripts to manage database schema changes and versioning.
    # Use Alembic commands to generate and apply migrations.
    # Test the migration process by adding new models and fields, then generating and applying the corresponding migration scripts.
    # Document the migration steps and any challenges faced during the process.
    