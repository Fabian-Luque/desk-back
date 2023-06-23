import logging
import uvicorn
from pathlib import Path
from fastapi import FastAPI, Depends

from config.db import initiate_database

from routes.user import user
from routes.auth import auth
from routes.product import product

from docs import tags_metadata
from utils.deps import has_access
from utils.custom_logging import CustomizeLogger
from utils.app_exceptions import AppExceptionCase
from utils.app_exceptions import app_exception_handler

logger = logging.getLogger(__name__)
config_path=Path(__file__).with_name("logging_config.json")
logger = CustomizeLogger.make_logger(config_path)

PROTECTED = [Depends(has_access)]
VERSION = 'v1'
PREFIX = '/api/'

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


app.include_router(
    user,
    prefix=PREFIX+VERSION,
    dependencies=PROTECTED
)
app.include_router(auth, prefix=PREFIX+VERSION)
app.include_router(product, prefix=PREFIX+VERSION)

app.logger = logger

# logger.info("info")
# app.logger.error("error")
# app.logger.warning("warning")