from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    astradb_keyspace: str = Field(..., env="ASTRADB_KEYSPACE")  # type: ignore
    astradb_client_id: str = Field(..., env="ASTRADB_CLIENT_ID")  # type: ignore # Update field name
    astradb_client_secret: str = Field(..., env="ASTRADB_CLIENT_SECRET")  # type: ignore

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()  # type: ignore
