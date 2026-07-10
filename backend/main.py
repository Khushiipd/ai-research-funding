from fastapi import FastAPI
from database import engine, Base
from routes.auth import router as auth_router
import models

app = FastAPI()

app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "AI Funding Platform Backend Running"
    }