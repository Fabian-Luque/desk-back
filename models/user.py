from typing import Optional, Any
from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    name: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdul@school.com",
                "password": "anithing",
            }
        }

class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

    class Collection:
        name = "User"
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdul@school.com",
                "password": "anithing",
            }
        }

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }