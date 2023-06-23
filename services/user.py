from passlib.hash import sha256_crypt
from bson import ObjectId

from services.main import AppService
from schemas.user import userEntity, usersEntity
from utils.service_result import ServiceResult
from utils.app_exceptions import AppException
from database.user import *

class UserService(AppService):
    async def find_all_users(self) -> ServiceResult:
        results = usersEntity(await find_all_users())
        if not results:
            return ServiceResult(AppException.GetItem())
        return ServiceResult(results)

    async def insert_one(self, user: userEntity) -> ServiceResult:
        result = userEntity(await insert_one(user))
        if not result:
            return ServiceResult(AppException.CreateItem())
        return ServiceResult(result)
    
    async def find_one(self, id: str) -> ServiceResult:
        result = userEntity(await find_one(id))
        if not result:
            return ServiceResult(AppException.GetItem())
        return ServiceResult(result)

    async def delete(self, id: str):
        result = await delete(self.db, id)
        if not result:
            return ServiceResult(AppException.DeleteItem())
        return ServiceResult(result)

    async def find_one_by_email(self, email: str) -> ServiceResult:
        result = await find_one_by_email(email)
        if not result:
            return ServiceResult(AppException.GetItem())
        return ServiceResult(result)