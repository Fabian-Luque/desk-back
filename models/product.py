from typing import Optional, Any
from beanie import Document
from pydantic import BaseModel
from datetime import datetime

class Product(Document):
    title: str
    description: str
    price: float
    discount: int
    rating: int
    brand: str
    color: str
    reviews: int
    image: list[Any]
    slug: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                'title': "Mens's Exclusive Watch",
                'description': 'Lorem ipsum',
                'price': 120.00,
                'discount': '25',
                'rating': 5,
                'brand': 1,
                'color': 'blue',
                'reviews': 2000,
                'slug': 'mens-exclusive-watch',
                'image': [
                    {
                        'src': 'path/to/img.jpg',
                    },
                ],
            }
        }

class UpdateUserModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    discount: Optional[int]
    rating: Optional[int]
    brand: Optional[str]
    color: Optional[str]
    reviews: Optional[int]
    image: Optional[list[Any]]
    slug: Optional[str]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Collection:
        name = "Product"
    
    class Config:
        schema_extra = {
            "example": {
                'title': "Mens's Exclusive Watch",
                'description': 'Lorem ipsum',
                'price': 120.00,
                'discount': '25',
                'rating': 5,
                'brand': 1,
                'color': 'blue',
                'reviews': 2000,
                'slug': 'mens-exclusive-watch',
                'image': [
                    {
                        'src': 'path/to/img.jpg',
                    },
                ],
            }
        }


class ResponseProduct(BaseModel):
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    discount: Optional[int]
    rating: Optional[int]
    brand: Optional[str]
    color: Optional[str]
    reviews: Optional[int]
    image: Optional[list[Any]]
    slug: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                'title': "Mens's Exclusive Watch",
                'description': 'Lorem ipsum',
                'price': 120.00,
                'discount': '25',
                'rating': 5,
                'brand': 1,
                'color': 'blue',
                'reviews': 2000,
                'slug': 'mens-exclusive-watch',
                'image': [
                    {
                        'src': 'path/to/img.jpg',
                    },
                ],
            }
        }