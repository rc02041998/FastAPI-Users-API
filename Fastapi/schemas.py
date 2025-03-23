from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str  # Accept raw password

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str  # Return raw password (Not recommended)

    class Config:
        orm_mode = True
