from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy import Column, Integer, String, create_engine, text, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import List, Optional
import re

# MySQL database configuration
MYSQL_PASSWORDS = ["", "root", "pa55worD$#pa", "123456", "admin"]

def get_database_url():
    """Try different passwords and return working DATABASE_URL"""
    for password in MYSQL_PASSWORDS:
        if password:
            url = f"mysql+pymysql://root:{password}@localhost:3306/hr_management"
        else:
            url = "mysql+pymysql://root@localhost:3306/hr_management"
        
        try:
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
    echo=True,
    pool_pre_ping=True,
    pool_recycle=300
)

# Create database if it doesn't exist
def create_database_if_not_exists():
    """Create the hr_management database if it doesn't exist"""
    try:
        engine.connect()
        print("✅ Database 'hr_management' exists and is accessible")
    except Exception as e:  
        if "Unknown database" in str(e) or "database doesn't exist" in str(e):
            print("📝 Creating database 'hr_management'...")
            base_url = DATABASE_URL.rsplit('/', 1)[0]
            temp_engine = create_engine(base_url)
            with temp_engine.connect() as conn:
                conn.execute(text("CREATE DATABASE IF NOT EXISTS hr_management"))
                conn.commit()
            print("✅ Database 'hr_management' created successfully")
        else:
            raise e

create_database_if_not_exists()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# =============================================================================
# DATABASE MODELS
# =============================================================================

class Organization(Base):
    __tablename__ = "organizations"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500))
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(200))
    website = Column(String(100))
    founded_year = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    departments = relationship("Department", back_populates="organization", cascade="all, delete-orphan")

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500))
    budget = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign Keys
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    manager_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    
    # Relationships
    organization = relationship("Organization", back_populates="departments")
    manager = relationship("Employee", foreign_keys=[manager_id], back_populates="managed_department")
    employees = relationship("Employee", foreign_keys="Employee.department_id", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    position = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)
    hire_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign Keys
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    
    # Relationships
    department = relationship("Department", foreign_keys=[department_id], back_populates="employees")
    managed_department = relationship("Department", foreign_keys="Department.manager_id", back_populates="manager")

# Create tables
Base.metadata.create_all(bind=engine)

# =============================================================================
# PYDANTIC SCHEMAS
# =============================================================================

# Organization Schemas
class OrganizationBase(BaseModel):
    name: str
    description: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    website: Optional[str] = None
    founded_year: Optional[int] = None
    
    @validator('founded_year')
    def validate_founded_year(cls, v):
        if v and (v < 1800 or v > datetime.now().year):
            raise ValueError('Founded year must be between 1800 and current year')
        return v

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    website: Optional[str] = None
    founded_year: Optional[int] = None
    is_active: Optional[bool] = None

class OrganizationRead(OrganizationBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Department Schemas
class DepartmentBase(BaseModel):
    name: str
    description: Optional[str] = None
    budget: Optional[float] = 0.0
    organization_id: int
    manager_id: Optional[int] = None
    
    @validator('budget')
    def validate_budget(cls, v):
        if v < 0:
            raise ValueError('Budget cannot be negative')
        return v

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    budget: Optional[float] = None
    manager_id: Optional[int] = None
    is_active: Optional[bool] = None

class DepartmentRead(DepartmentBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Employee Schemas
class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    position: str
    salary: float
    department_id: int
    
    @validator('salary')
    def validate_salary(cls, v):
        if v < 0:
            raise ValueError('Salary cannot be negative')
        return v
    
    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        if not re.match(r"^[A-Za-z\s]+$", v):
            raise ValueError('Names can only contain letters and spaces')
        return v

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
    department_id: Optional[int] = None
    is_active: Optional[bool] = None

class EmployeeRead(EmployeeBase):
    id: int
    hire_date: datetime
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# =============================================================================
# FASTAPI APP SETUP
# =============================================================================

app = FastAPI(
    title="HR Management System API",
    description="A comprehensive CRUD API for managing organizations, departments, and employees",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def get_organization_or_404(db: Session, org_id: int):
    org = db.query(Organization).filter(Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org

def get_department_or_404(db: Session, dept_id: int):
    dept = db.query(Department).filter(Department.id == dept_id).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept

def get_employee_or_404(db: Session, emp_id: int):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# =============================================================================
# ROOT AND HEALTH ENDPOINTS
# =============================================================================

@app.get("/")
def read_root():
    return {
        "message": "Welcome to HR Management System API",
        "database": "MySQL",
        "endpoints": {
            "organizations": "/organizations/",
            "departments": "/departments/",
            "employees": "/employees/",
            "docs": "/docs"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint to verify database connection"""
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

# =============================================================================
# ORGANIZATION CRUD ENDPOINTS
# =============================================================================

@app.post("/organizations/", response_model=OrganizationRead)
def create_organization(org: OrganizationCreate, db: Session = Depends(get_db)):
    """Create a new organization"""
    # Check if organization with same email exists
    existing_org = db.query(Organization).filter(Organization.email == org.email).first()
    if existing_org:
        raise HTTPException(status_code=400, detail="Organization with this email already exists")
    
    db_org = Organization(**org.dict())
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

@app.get("/organizations/", response_model=List[OrganizationRead])
def read_organizations(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of records to return"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    db: Session = Depends(get_db)
):
    """Get all organizations with optional filtering"""
    query = db.query(Organization)
    
    if is_active is not None:
        query = query.filter(Organization.is_active == is_active)
    
    organizations = query.offset(skip).limit(limit).all()
    return organizations

@app.get("/organizations/{org_id}", response_model=OrganizationRead)
def read_organization(org_id: int, db: Session = Depends(get_db)):
    """Get a specific organization by ID"""
    return get_organization_or_404(db, org_id)

@app.put("/organizations/{org_id}", response_model=OrganizationRead)
def update_organization(org_id: int, org_update: OrganizationUpdate, db: Session = Depends(get_db)):
    """Update an organization"""
    db_org = get_organization_or_404(db, org_id)
    
    # Check email uniqueness if email is being updated
    if org_update.email and org_update.email != db_org.email:
        existing_org = db.query(Organization).filter(Organization.email == org_update.email).first()
        if existing_org:
            raise HTTPException(status_code=400, detail="Organization with this email already exists")
    
    update_data = org_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_org, field, value)
    
    db.commit()
    db.refresh(db_org)
    return db_org

@app.delete("/organizations/{org_id}")
def delete_organization(org_id: int, db: Session = Depends(get_db)):
    """Delete an organization and all its departments/employees"""
    db_org = get_organization_or_404(db, org_id)
    db.delete(db_org)
    db.commit()
    return {"detail": "Organization deleted successfully"}

# =============================================================================
# DEPARTMENT CRUD ENDPOINTS
# =============================================================================

@app.post("/departments/", response_model=DepartmentRead)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
    """Create a new department"""
    # Verify organization exists
    get_organization_or_404(db, dept.organization_id)
    
    # Verify manager exists if provided
    if dept.manager_id:
        get_employee_or_404(db, dept.manager_id)
    
    db_dept = Department(**dept.dict())
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

@app.get("/departments/", response_model=List[DepartmentRead])
def read_departments(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    organization_id: Optional[int] = Query(None, description="Filter by organization ID"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    db: Session = Depends(get_db)
):
    """Get all departments with optional filtering"""
    query = db.query(Department)
    
    if organization_id:
        query = query.filter(Department.organization_id == organization_id)
    
    if is_active is not None:
        query = query.filter(Department.is_active == is_active)
    
    departments = query.offset(skip).limit(limit).all()
    return departments

@app.get("/departments/{dept_id}", response_model=DepartmentRead)
def read_department(dept_id: int, db: Session = Depends(get_db)):
    """Get a specific department by ID"""
    return get_department_or_404(db, dept_id)

@app.put("/departments/{dept_id}", response_model=DepartmentRead)
def update_department(dept_id: int, dept_update: DepartmentUpdate, db: Session = Depends(get_db)):
    """Update a department"""
    db_dept = get_department_or_404(db, dept_id)
    
    # Verify manager exists if provided
    if dept_update.manager_id:
        get_employee_or_404(db, dept_update.manager_id)
    
    update_data = dept_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_dept, field, value)
    
    db.commit()
    db.refresh(db_dept)
    return db_dept

@app.delete("/departments/{dept_id}")
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    """Delete a department and all its employees"""
    db_dept = get_department_or_404(db, dept_id)
    db.delete(db_dept)
    db.commit()
    return {"detail": "Department deleted successfully"}

# =============================================================================
# EMPLOYEE CRUD ENDPOINTS
# =============================================================================

@app.post("/employees/", response_model=EmployeeRead)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new employee"""
    # Verify department exists
    get_department_or_404(db, emp.department_id)
    
    # Check if employee with same email exists
    existing_emp = db.query(Employee).filter(Employee.email == emp.email).first()
    if existing_emp:
        raise HTTPException(status_code=400, detail="Employee with this email already exists")
    
    db_emp = Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

@app.get("/employees/", response_model=List[EmployeeRead])
def read_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    department_id: Optional[int] = Query(None, description="Filter by department ID"),
    position: Optional[str] = Query(None, description="Filter by position"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    db: Session = Depends(get_db)
):
    """Get all employees with optional filtering"""
    query = db.query(Employee)
    
    if department_id:
        query = query.filter(Employee.department_id == department_id)
    
    if position:
        query = query.filter(Employee.position.ilike(f"%{position}%"))
    
    if is_active is not None:
        query = query.filter(Employee.is_active == is_active)
    
    employees = query.offset(skip).limit(limit).all()
    return employees

@app.get("/employees/{emp_id}", response_model=EmployeeRead)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    """Get a specific employee by ID"""
    return get_employee_or_404(db, emp_id)

@app.put("/employees/{emp_id}", response_model=EmployeeRead)
def update_employee(emp_id: int, emp_update: EmployeeUpdate, db: Session = Depends(get_db)):
    """Update an employee"""
    db_emp = get_employee_or_404(db, emp_id)
    
    # Check email uniqueness if email is being updated
    if emp_update.email and emp_update.email != db_emp.email:
        existing_emp = db.query(Employee).filter(Employee.email == emp_update.email).first()
        if existing_emp:
            raise HTTPException(status_code=400, detail="Employee with this email already exists")
    
    # Verify department exists if department is being updated
    if emp_update.department_id:
        get_department_or_404(db, emp_update.department_id)
    
    update_data = emp_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_emp, field, value)
    
    db.commit()
    db.refresh(db_emp)
    return db_emp

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    """Delete an employee"""
    db_emp = get_employee_or_404(db, emp_id)
    db.delete(db_emp)
    db.commit()
    return {"detail": "Employee deleted successfully"}

# =============================================================================
# RELATIONSHIP ENDPOINTS
# =============================================================================

@app.get("/organizations/{org_id}/departments", response_model=List[DepartmentRead])
def get_organization_departments(org_id: int, db: Session = Depends(get_db)):
    """Get all departments for a specific organization"""
    get_organization_or_404(db, org_id)  # Verify organization exists
    departments = db.query(Department).filter(Department.organization_id == org_id).all()
    return departments

@app.get("/departments/{dept_id}/employees", response_model=List[EmployeeRead])
def get_department_employees(dept_id: int, db: Session = Depends(get_db)):
    """Get all employees for a specific department"""
    get_department_or_404(db, dept_id)  # Verify department exists
    employees = db.query(Employee).filter(Employee.department_id == dept_id).all()
    return employees

@app.get("/organizations/{org_id}/employees", response_model=List[EmployeeRead])
def get_organization_employees(org_id: int, db: Session = Depends(get_db)):
    """Get all employees for a specific organization"""
    get_organization_or_404(db, org_id)  # Verify organization exists
    employees = db.query(Employee).join(Department).filter(
        Department.organization_id == org_id
    ).all()
    return employees

# =============================================================================
# ANALYTICS ENDPOINTS
# =============================================================================

@app.get("/analytics/summary")
def get_analytics_summary(db: Session = Depends(get_db)):
    """Get summary analytics for the HR system"""
    total_orgs = db.query(Organization).count()
    active_orgs = db.query(Organization).filter(Organization.is_active == True).count()
    total_depts = db.query(Department).count()
    active_depts = db.query(Department).filter(Department.is_active == True).count()
    total_employees = db.query(Employee).count()
    active_employees = db.query(Employee).filter(Employee.is_active == True).count()
    
    return {
        "organizations": {"total": total_orgs, "active": active_orgs},
        "departments": {"total": total_depts, "active": active_depts},
        "employees": {"total": total_employees, "active": active_employees}
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
