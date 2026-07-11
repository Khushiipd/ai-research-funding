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

@router.post("/publication")
def create_publication(
    publication: schemas.PublicationCreate,
    db: Session = Depends(get_db)
):

    new_publication = models.Publication(
        user_id=publication.user_id,
        title=publication.title,
        authors=publication.authors,
        journal=publication.journal,
        year=publication.year,
        doi=publication.doi
    )

    db.add(new_publication)
    db.commit()
    db.refresh(new_publication)

    return {
        "message": "Publication added successfully"
    }

@router.post("/patent")
def create_patent(
    patent: schemas.PatentCreate,
    db: Session = Depends(get_db)
):

    new_patent = models.Patent(
        user_id=patent.user_id,
        patent_title=patent.patent_title,
        patent_number=patent.patent_number,
        status=patent.status,
        filing_year=patent.filing_year
    )

    db.add(new_patent)
    db.commit()
    db.refresh(new_patent)

    return {
        "message": "Patent added successfully"
    }