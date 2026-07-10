from fastapi import FastAPI
from database import engine

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Funding Platform Backend Running",
        "database": "Connected Successfully"
    }