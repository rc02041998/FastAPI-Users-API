from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import models
from database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Unified endpoint with flag
@router.post("/")
def handle_users(
    input: str = Query(..., description="Use 'I' for Insert and 'G' for Get"),
    name: str = None,
    email: str = None,
    password: str = None,
    db: Session = Depends(get_db)
):
    if input == "I":
        # if not name or not email or not password:
        #     raise HTTPException(status_code=400, detail="Name, email, and password are required for insertion")
        db_user = models.User(name=name, email=email, password=password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"CODE":"200","MESSAGE": "User created successfully", "id": db_user.id, "name": db_user.name, "email": db_user.email}

    elif input == "G":
        users = db.query(models.User).all()
        return {"CODE":"200", "MESSAGE": "User fetched successfully","users": users}

    else:
        raise HTTPException(status_code=400, detail="Invalid input flag. Use 'I' for Insert and 'G' for Get.")
