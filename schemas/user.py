def userEntity(item) -> dict:
    return {
        "id": str(item.id),
        "name": item.name,
        "email": item.email,
        "password": item.password,
        "test": item.email
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]