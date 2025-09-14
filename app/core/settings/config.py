from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    debug: bool

    db_dialect: str
    db_port: int
    db_host: str
    db_user: str
    db_password: str
    db_name: str

    def __init__(self):
        super().__init__()

    @computed_field
    @property
    def db_url(self) -> str:
        return f"{self.db_dialect}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @computed_field
    @property
    def db_alembic_url(self) -> str:
        return f"{self.db_dialect}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file=".env.dev")


@lru_cache
def get_settings():
    return Settings()
