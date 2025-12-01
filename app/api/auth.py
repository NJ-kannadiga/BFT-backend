from datetime import datetime
from typing import Dict

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app import schemas

router = APIRouter()

# In-memory user store (resets every time server restarts)
# key: user_id, value: user dict
users: Dict[int, dict] = {
    1: {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
        "password": "password1",  # ⚠️ plain text, OK only for demo
        "created_at": datetime.utcnow(),
    },
    2: {
        "id": 2,
        "username": "bob",
        "email": "bob@example.com",
        "password": "password2",
        "created_at": datetime.utcnow(),
    },
    3: {
        "id": 3,
        "username": "carol",
        "email": "carol@example.com",
        "password": "password3",
        "created_at": datetime.utcnow(),
    },
    4: {
        "id": 4,
        "username": "dave",
        "email": "dave@example.com",
        "password": "password4",
        "created_at": datetime.utcnow(),
    },
    5: {
        "id": 5,
        "username": "eve",
        "email": "eve@example.com",
        "password": "password5",
        "created_at": datetime.utcnow(),
    },
}
next_user_id: int = 6


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/register", response_model=schemas.UserOut)
def register(user_in: schemas.UserCreate):
    global next_user_id

    # Check if username or email already exists
    for u in users.values():
        if u["username"] == user_in.username:
            raise HTTPException(status_code=400, detail="Username already exists")
        if u["email"] == user_in.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    # Create user in memory
    user_data = {
        "id": next_user_id,
        "username": user_in.username,
        "email": user_in.email,
        "password": user_in.password,  # ⚠️ plain text, OK only for demo
        "created_at": datetime.utcnow(),
    }

    users[next_user_id] = user_data
    next_user_id += 1

    # Return only fields defined in UserOut
    return schemas.UserOut(
        id=user_data["id"],
        username=user_data["username"],
        email=user_data["email"],
        created_at=user_data["created_at"],
    )


@router.post("/login")
def login(payload: LoginRequest):
    # Find user by username
    for u in users.values():
        if u["username"] == payload.username:
            if u["password"] == payload.password:
                return {
                    "msg": "Login successful",
                    "user": {
                        "id": u["id"],
                        "username": u["username"],
                        "email": u["email"],
                        "created_at": u["created_at"],
                    },
                }
            break

    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.get("/users", response_model=list[schemas.UserOut])
def list_users():
    return [
        schemas.UserOut(
            id=u["id"],
            username=u["username"],
            email=u["email"],
            created_at=u["created_at"],
        )
        for u in users.values()
    ]
