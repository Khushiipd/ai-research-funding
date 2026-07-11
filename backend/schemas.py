from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str

class ResearchProfileCreate(BaseModel):
    user_id: int
    organization: str
    designation: str
    research_domain: str
    experience: str
    skills: str
    bio: str

class PublicationCreate(BaseModel):
    user_id: int
    title: str
    authors: str
    journal: str
    year: str
    doi: str

class PatentCreate(BaseModel):
    user_id: int
    patent_title: str
    patent_number: str
    status: str
    filing_year: str