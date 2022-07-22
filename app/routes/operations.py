import logging

from fastapi import APIRouter, status

from app.models.operations import (
    Urls,
    Urls_Pydantic,
    UrlOriginal,
)

logger = logging.getLogger('url-shortener-log')

router = APIRouter(
    prefix='/operations',
    tags=['Operations']
)


@router.post('/url-shorten', status_code=status.HTTP_201_CREATED)
async def shorten_url(url: UrlOriginal):
    try:
        url_original = url.url_original

        obj = await Urls.create(
            url_original=url_original,
            url_shorten="Test",
        )
        return await Urls_Pydantic.from_tortoise_orm(obj)
    except Exception as e:
        logger.error(f'{e}')


@router.get('/url-original/{url_shorten}')
async def original_url(url_shorten: str):
    obj = await Urls.get(url_shorten=url_shorten)
    return await Urls_Pydantic.from_tortoise_orm(obj)
