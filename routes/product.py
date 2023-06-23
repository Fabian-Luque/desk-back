from fastapi import APIRouter, Response, status, Depends

from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from models.product import *
from services.product import ProductService
from utils.service_result import handle_result
product = APIRouter()


@product.get("/products", response_model=list[ResponseProduct], tags=["products"])
async def find_all_products():
    result = await ProductService().find_all()
    return handle_result(result)


@product.post("/products", response_model=ResponseProduct, tags=["products"])
async def create(product: Product):
    result = await ProductService().insert_one(product)
    return handle_result(result)


@product.get("/products/{id}", response_model=ResponseProduct, tags=["products"])
async def find_product(id: str):
    result = await ProductService().find_one(id)
    return handle_result(result)


@product.put("/products/{id}", response_model=ResponseProduct, tags=["products"])
async def update(id: str, product: Product):
    result = await ProductService().update(id, product)
    return handle_result(result)

@product.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["products"])
async def delete(id: str):
    await ProductService().delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)
