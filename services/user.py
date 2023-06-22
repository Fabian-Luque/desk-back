from passlib.hash import sha256_crypt
from bson import ObjectId

from services.main import AppService
from schemas.user import userEntity
from utils.service_result import ServiceResult
from utils.app_exceptions import AppException
from database.user import *

class UserService(AppService):
    async def find_all_users(self) -> ServiceResult:
        results = await find_all_users()
        if not results:
            return ServiceResult(AppException.GetItem())
        return ServiceResult(results)

    async def insert_one(self, user: userEntity) -> ServiceResult:
        result = await insert_one(user)
        if not result:
            return ServiceResult(AppException.CreateItem())
        return ServiceResult(result)
    
    def find_one(self, id: str) -> ServiceResult:
        result = UserCRUD(self.db).find_one(id)
        if not result:
            return ServiceResult(AppException.GetItem())
        return ServiceResult(result)

    def delete(self, id: str):
        result = UserCRUD.delete(self.db, id)
        if not result:
            return ServiceResult(AppException.DeleteItem())
        return ServiceResult(result)

class UserCRUD():
    def find_all_users(self) -> [userEntity]:
        return self.db.local.user.find()

    def insert_one(self, user: userEntity) -> userEntity:
        new_user = dict(user)
        new_user["password"] = sha256_crypt.encrypt(new_user["password"])
        del new_user["id"]
        id = self.local.user.insert_one(new_user).inserted_id
        return self.local.user.find_one({"_id": id})

    def find_one(self, id: str) -> userEntity:
        return self.db.local.user.find_one({"_id": ObjectId(id)})

    def update(self, id: str, user: userEntity) -> userEntity:
        self.db.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
        return self.db.local.user.find_one({"_id": ObjectId(id)})

    def delete(self, id: str):
        self.local.user.find_one_and_delete({"_id": ObjectId(id)})