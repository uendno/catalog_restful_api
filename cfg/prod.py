from .base import _Config


class _ProdConfig(_Config):
    SQL_ALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://robert:robert@localhost/catalog_db'
    DEBUG = False


config = _ProdConfig
