# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from datetime import datetime, timedelta
# from app.db import get_db
# from app.api.auth import get_current_user
# from app import models
# from sqlalchemy import func

# router = APIRouter()

# @router.get("/monthly")
# def monthly_summary(month: int = None, year: int = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
#     # default to current month
#     now = datetime.utcnow()
#     if not month: month = now.month
#     if not year: year = now.year
#     start = datetime(year, month, 1)
#     if month == 12:
#         end = datetime(year+1, 1, 1)
#     else:
#         end = datetime(year, month+1, 1)

#     total_income = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.user_id==user.id, models.Transaction.date >= start, models.Transaction.date < end, models.Transaction.amount>0).scalar() or 0
#     total_expense = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.user_id==user.id, models.Transaction.date >= start, models.Transaction.date < end, models.Transaction.amount<0).scalar() or 0
#     return {"income": total_income, "expense": total_expense}
