import os

import dotenv
from pydantic import BaseModel

dotenv.load_dotenv()


class DataBase(BaseModel):
    port: int = os.environ.get("POSTGRES_PORT")
    host: str = os.environ.get("POSTGRES_HOST")
    name: str = os.environ.get("POSTGRES_DB")
    password: str = os.environ.get("POSTGRES_PASSWORD")
    user: str = os.environ.get("POSTGRES_USER")
    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"


class Settings(BaseModel):
    db: DataBase = DataBase()


settings = Settings()
