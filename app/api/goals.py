from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.utils.security import get_current_user
import app.schemas as schemas
import app.models as models


router = APIRouter()

@router.get("/", response_model=list[schemas.GoalOut])
def get_goals(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(models.Goal).filter(models.Goal.user_id == current_user.id).all()


@router.post("/", response_model=schemas.GoalOut)
def create_goal(goal: schemas.GoalCreate, 
                db: Session = Depends(get_db), 
                current_user=Depends(get_current_user)):

    new_goal = models.Goal(
        title=goal.title,
        type=goal.type,
        target_amount=goal.target_amount,
        deadline=goal.deadline,
        user_id=current_user.id
    )

    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal
