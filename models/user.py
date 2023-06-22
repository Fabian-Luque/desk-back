from typing import Optional
from pydantic import BaseModel
from config.db import db

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

