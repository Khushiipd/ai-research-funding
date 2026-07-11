from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ResearchProfile(Base):
    __tablename__ = "research_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    organization = Column(String)
    designation = Column(String)
    research_domain = Column(String)
    experience = Column(String)
    skills = Column(String)
    bio = Column(String)

    user = relationship("User")

class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    title = Column(String)
    authors = Column(String)
    journal = Column(String)
    year = Column(String)
    doi = Column(String)

    user = relationship("User")

class Patent(Base):
    __tablename__ = "patents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    patent_title = Column(String)
    patent_number = Column(String)
    status = Column(String)
    filing_year = Column(String)

    user = relationship("User")