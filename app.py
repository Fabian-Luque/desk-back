import logging
from fastapi import FastAPI

from routes.user import user
from utils.app_exceptions import AppExceptionCase
from docs import tags_metadata
from utils.app_exceptions import app_exception_handler
from config.db import initiate_database

logging.config.fileConfig
logging.config.fileConfig('config/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__) 
logger.info("logging from the root logger")

app = FastAPI(
    title="REAT API Fast Api and Mongodb",
    description="This is a simple REST API with fastapi and  mongodb",
    version="0.0.1",
    openapi_tags=tags_metadata
)

@app.on_event("startup")
async def start_database():
    await initiate_database()

@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(user)