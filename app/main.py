import logging
from logging.config import dictConfig

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.config.db import DB_CONFIG
from app.config.settings import LogConfig
from app.config.settings import Settings
from app.routes import operations


dictConfig(LogConfig().dict())
logger = logging.getLogger('url-shortener-log')

prefix = '/api/v1'

settings = Settings()
app = FastAPI(title=settings.APP_NAME)

app.include_router(operations.router, prefix=prefix)


@app.get("/health-check")
async def health_check():
    return {"status": "Running..."}


register_tortoise(
    app,
    config=DB_CONFIG,
    modules={'models': ['app.models.operations']},
    generate_schemas=True,
    add_exception_handlers=True
)
