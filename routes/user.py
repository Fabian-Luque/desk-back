from fastapi import APIRouter, Response, status, Depends

from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from models.user import *
from services.user import UserService
from utils.service_result import handle_result
from utils.deps import get_current_user
user = APIRouter()


@user.get("/users", dependencies=[Depends(get_current_user)], response_model=list[ResponseUser], tags=["users"])
async def find_all_users():
    result = await UserService().find_all_users()
    return handle_result(result)


@user.post("/users", response_model=ResponseUser, tags=["users"])
async def create_user(user: User):
    result = await UserService().insert_one(user)
    return handle_result(result)


@user.get("/users/{id}", response_model=ResponseUser, tags=["users"])
async def find_user(id: str, me = Depends(get_current_user)):
    result = await UserService().find_one(id)
    return handle_result(result)


@user.put("/users/{id}", response_model=ResponseUser, tags=["users"])
async def update_user(id: str, user: User):
    result = await UserService().update_user(id, user)
    return handle_result(result)

@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(id: str):
    await UserService().delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)
