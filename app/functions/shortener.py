import logging
import string
import secrets

from app.config.settings import get_settings

settings = get_settings()
logger = logging.getLogger('url-shortener-log')


def generate_code(length: int = 5) -> str:
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))
