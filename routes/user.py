from fastapi import APIRouter, Response, status

from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from schemas.user import userEntity, usersEntity
from models.user import User
from services.user import UserService
from utils.service_result import handle_result
user = APIRouter()


@user.get("/users", response_model=list[User], tags=["users"])
async def find_all_users():
    result = await UserService().find_all_users()
    return handle_result(result)


@user.post("/users", response_model=User, tags=["users"])
async def create_user(user: User):
    result = await UserService().insert_one(user)
    return handle_result(result)


@user.get("/users/{id}", response_model=User, tags=["users"])
def find_user(id: str):
    result = UserService().find_one(id)
    return userEntity(handle_result(result))


@user.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id: str, user: User):
    # db.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    # return userEntity(db.local.user.find_one({"_id": ObjectId(id)}))
    result = UserService().update_user(id, user)
    return handle_result(result)

@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    # userEntity(db.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    UserService().delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)
