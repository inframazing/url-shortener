from functools import lru_cache
from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    APP_NAME = 'url-shortener'
    MODELS = [
        'aerich.models',
        'app.models.operations',
    ]

    class Config:
        case_sensitive: bool = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


class LogConfig(BaseModel):
    LOGGER_NAME: str = "url-shortener-log"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "url-shortener-log": {"handlers": ["default"], "level": LOG_LEVEL},
    }


@lru_cache()
def get_settings():
    return Settings()
