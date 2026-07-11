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

@router.post("/profile")
def create_profile(profile: schemas.ResearchProfileCreate,
                   db: Session = Depends(get_db)):

    new_profile = models.ResearchProfile(
        user_id=profile.user_id,
        organization=profile.organization,
        designation=profile.designation,
        research_domain=profile.research_domain,
        experience=profile.experience,
        skills=profile.skills,
        bio=profile.bio
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return {
        "message": "Research profile created successfully"
    }