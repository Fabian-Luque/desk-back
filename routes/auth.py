from fastapi import APIRouter, Response, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from services.user import UserService
from utils.service_result import handle_result
from schemas.token import Token
from utils.crypto import *
from models.user import *
from utils.jwt import *

auth = APIRouter()

@auth.post('/signup', response_model=ResponseUser, tags=["auth"])
async def create_user(user: User):
    user_found = await UserService().find_one_by_email(user.email)

    if user_found.success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exist"
            )
    user.password = get_hashed_password(user.password)
    result = await UserService().insert_one(user)
    return handle_result(result)

@auth.post('/login', summary="Create access and refresh tokens for user", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await UserService().find_one_by_email(form_data.username)
    if user.success is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    user = handle_result(user)
    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }