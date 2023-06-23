from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    refresh_token: str
    
class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None

class UserOut(BaseModel):
    id: str
    email: str

class SystemUser(UserOut):
    password: str