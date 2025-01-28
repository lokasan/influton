from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import root_validator


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str

    @root_validator(skip_on_failure=True)
    def get_db(cls, v):
        v['DATABASE_URL'] = f'postgresql+asyncpg://{v["DB_USER"]}:{v["DB_PASS"]}@{v["DB_HOST"]}:{v["DB_PORT"]}/{v["DB_NAME"]}'
        return v

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
