from fastapi import FastAPI

from routes.user import user

from docs import tags_metadata

app = FastAPI(
    title="REAT API Fast Api and Mongodb",
    description="This is a simple REST API with fastapi and  mongodb",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(user)

