# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from typing import List
# from app import models, schemas
# from app.db import get_db, engine
# from app.api.auth import get_current_user
# models.Base.metadata.create_all(bind=engine)

# router = APIRouter()

# @router.post("/", response_model=schemas.CategoryOut)
# def create_category(c_in: schemas.CategoryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
#     c = models.Category(**c_in.dict())
#     db.add(c); db.commit(); db.refresh(c)
#     return c

# @router.get("/", response_model=List[schemas.CategoryOut])
# def list_categories(db: Session = Depends(get_db), user=Depends(get_current_user)):
#     return db.query(models.Category).all()
