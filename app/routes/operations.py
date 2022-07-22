import logging

from fastapi import APIRouter, status

from app.models.operations import (
    Urls,
    Urls_Pydantic,
    UrlsBody,
)

logger = logging.getLogger('url-shortener-log')

router = APIRouter(
    prefix='/operations',
    tags=['Operations']
)


@router.post('/shorten-url', status_code=status.HTTP_201_CREATED)
async def shorten_url(urls: UrlsBody):
    try:
        original_url = urls.original_url
        shortener_url = urls.shortener_url

        obj = await Urls.create(
            original_url=original_url,
            shortener_url=shortener_url
        )
        return await Urls_Pydantic.from_tortoise_orm(obj)
    except Exception as e:
        logger.error(f'{e}')
