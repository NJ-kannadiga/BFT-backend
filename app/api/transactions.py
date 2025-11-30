# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from app import models, schemas
# from app.db import get_db, engine
# from app.api.auth import get_current_user, oauth2_scheme
# models.Base.metadata.create_all(bind=engine)

# router = APIRouter()

# @router.post("/", response_model=schemas.TransactionOut)
# def create_transaction(tx_in: schemas.TransactionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
#     tx = models.Transaction(**tx_in.dict(), user_id=user.id)
#     db.add(tx); db.commit(); db.refresh(tx)
#     # update account balance if account provided
#     if tx.account_id:
#         acc = db.query(models.Account).get(tx.account_id)
#         if acc:
#             acc.balance = (acc.balance or 0) + tx.amount
#             db.add(acc); db.commit()
#     return tx

# @router.get("/", response_model=List[schemas.TransactionOut])
# def list_transactions(skip: int = 0, limit: int = 50, db: Session = Depends(get_db), user=Depends(get_current_user)):
#     txs = db.query(models.Transaction).filter(models.Transaction.user_id==user.id).order_by(models.Transaction.date.desc()).offset(skip).limit(limit).all()
#     return txs
