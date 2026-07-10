from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully!"
    }