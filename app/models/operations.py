from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel


class Urls(Model):
    id = fields.IntField(pk=True)
    url_original = fields.CharField(max_length=150)
    url_shorten = fields.CharField(max_length=50, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'TA_Urls'


class UrlOriginal(BaseModel):
    url_original: str


Urls_Pydantic = pydantic_model_creator(Urls, name='Urls')
UrlsIn_Pydantic = pydantic_model_creator(
    Urls, name='urlsIn', exclude_readonly=True
)
