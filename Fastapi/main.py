from fastapi import FastAPI
from database import engine, Base
import models
from routers import users

app = FastAPI(title="FastAPI Users API")

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Include Users Router
app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}
