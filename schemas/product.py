def productEntity(item) -> dict:
    return {
        "id": str(item.id),
        "title": item.title,
        "description": item.description,
        "price": item.price,
        "discount": item.discount,
        "rating": item.rating,
        "brand": item.brand,
        "color": item.color,
        "reviews": item.reviews,
        "slug": item.slug,
        "image": item.image,
    }

def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]