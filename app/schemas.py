from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# ---------------- AUTH ----------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------------- ACCOUNT ----------------
class AccountCreate(BaseModel):
    name: str
    balance: Optional[float] = 0.0
    currency: Optional[str] = "INR"


class AccountOut(AccountCreate):
    id: int
    user_id: int
    class Config:
        from_attributes = True


# ---------------- CATEGORY ----------------
class CategoryCreate(BaseModel):
    name: str
    type: Optional[str] = "expense"


class CategoryOut(CategoryCreate):
    id: int
    class Config:
        from_attributes = True


# ---------------- TRANSACTION ----------------
class TransactionCreate(BaseModel):
    amount: float
    note: Optional[str] = None
    date: Optional[datetime] = None
    category_id: Optional[int] = None
    account_id: Optional[int] = None


class TransactionOut(TransactionCreate):
    id: int
    user_id: int
    class Config:
        from_attributes = True

# ---------------- GOALS ----------------
class GoalCreate(BaseModel):
    title: str
    type: str
    target_amount: float
    deadline: datetime


class GoalOut(GoalCreate):
    id: int
    user_id: int
    class Config:
        from_attributes = True