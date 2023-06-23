from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # auth configuration
    JWT_SECRET_KEY:  Optional[str] = 'salt'
    JWT_REFRESH_SECRET_KEY:  Optional[str] = 'salt'
    class Config:
        env_file = ".env.dev"