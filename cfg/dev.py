from .base import _Config


class _DevConfig(_Config):
    SQL_ALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://robert:robert@localhost/catalog_restful_api'
    DEBUG = True


config = _DevConfig
