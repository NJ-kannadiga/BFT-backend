from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.db import get_db, engine
users = {}

# Create tables
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    # check if user already exists
    existing = db.query(models.User).filter(
        (models.User.email == user_in.email) | (models.User.username == user_in.username)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    # no hashing, just store password directly (not secure, but simple)
    user = models.User(
        username=user_in.username,
        email=user_in.email,
        password=user_in.password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user



@router.post("/login")
def login(user):   # <-- expects a Pydantic model
    stored = users.get(user.username)
    if not stored or stored["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"msg": "Login successful", "user": stored}


@router.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
