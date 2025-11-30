# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from app import models, schemas
# from app.db import get_db, engine
# from app.api.auth import get_current_user
# models.Base.metadata.create_all(bind=engine)

# router = APIRouter()

# @router.post("/", response_model=schemas.AccountOut)
# def create_account(a_in: schemas.AccountCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
#     acc = models.Account(**a_in.dict(), user_id=user.id)
#     db.add(acc); db.commit(); db.refresh(acc)
#     return acc

# @router.get("/", response_model=List[schemas.AccountOut])
# def list_accounts(db: Session = Depends(get_db), user=Depends(get_current_user)):
#     return db.query(models.Account).filter(models.Account.user_id==user.id).all()
