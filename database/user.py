from typing import List, Union

from models.user import User
from beanie import PydanticObjectId
user_collecion = User

async def find_all_users() -> List[User]:
    users = await user_collecion.all().to_list()
    print(users)
    return users

async def insert_one(new_user: User) -> User:
    user = await new_user.create()
    return user

async def find_one(id: PydanticObjectId) -> User:
    user = await user_collecion.get(id)
    if user:
        return user

async def update_user_data(id: PydanticObjectId, data: dict) -> Union[bool, User]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in des_body.items()
    }}
    user = await user_collecion.get(id)
    if user:
        await user.update(update_query)
        return user
    return False


async def delete(id: PydanticObjectId) -> bool:
    user = await user_collecion.get(id)
    if user:
        await user.delete()
        return True