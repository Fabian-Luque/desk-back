from passlib.hash import sha256_crypt
from bson import ObjectId

from services.main import AppService

from schemas.product import productEntity, productsEntity

from utils.service_result import ServiceResult
from utils.app_exceptions import AppException
from database.product import *

class ProductService(AppService):
    async def find_all(self) -> ServiceResult:
        results = await find_all()
        if not results:
            return ServiceResult(AppException.GetItem())
        return ServiceResult(productsEntity(results))

    async def insert_one(self, product: productEntity) -> ServiceResult:
        result = await insert_one(product)
        if not result:
            return ServiceResult(AppException.CreateItem())
        return ServiceResult(productEntity(result))
    
    async def find_one(self, id: str) -> ServiceResult:
        result = await find_one(id)
        if not result:
            return ServiceResult(AppException.GetItem())
        return ServiceResult(productEntity(result))

    async def delete(self, id: str):
        result = await delete(id)
        if not result:
            return ServiceResult(AppException.DeleteItem())
        return ServiceResult(result)