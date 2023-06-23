from typing import List, Union

from models.product import Product
from beanie import PydanticObjectId
product_collecion = Product

async def find_all() -> List[Product]:
    products = await product_collecion.all().to_list()
    return products

async def insert_one(new_product: Product) -> Product:
    product = await new_product.create()
    return product

async def find_one(id: PydanticObjectId) -> Product:
    product = await product_collecion.get(id)
    if product:
        return product

async def update_product_data(id: PydanticObjectId, data: dict) -> Union[bool, Product]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in des_body.items()
    }}
    product = await product_collecion.get(id)
    if product:
        await product.update(update_query)
        return product
    return False


async def delete(id: PydanticObjectId) -> bool:
    product = await product_collecion.get(id)
    if product:
        await product.delete()
        return True