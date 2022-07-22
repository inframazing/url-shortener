from app.config.settings import get_settings

settings = get_settings()

DB_URL = (
    f'postgres://'
    f'{settings.DB_USER}:'
    f'{settings.DB_PASSWORD}@'
    f'{settings.DB_HOST}:'
    f'{settings.DB_PORT}/'
    f'{settings.DB_NAME}'
)

DB_CONFIG = {
    "connections": {"default": DB_URL},
    "apps": {settings.APP_NAME: {"models": settings.MODELS}},
    'use_tz': False,
    'timezone': 'UTC',
}
