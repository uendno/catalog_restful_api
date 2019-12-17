from .base import _Config


class _DevConfig(_Config):
    SQL_ALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@localhost/catalog_restful_api'
    DEBUG = True


config = _DevConfig
