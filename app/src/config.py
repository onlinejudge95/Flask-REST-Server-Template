"""
Configuration module for the app.
"""
import os
import pathlib
import uuid


class BaseConfig:
    TESTING = False
    BASE_DIR = pathlib.Path.cwd()
    SECRET_KEY = uuid.uuid4().hex


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    JSONIFY_PRETTYPRINT_REGULAR = True


class ProductionConfig(BaseConfig):
    JSONIFY_PRETTYPRINT_REGULAR = True


config_map = {
    "development": "app.src.config.DevelopmentConfig",
    "testing": "app.src.config.TestingConfig",
    "production": "app.src.config.ProductionConfig",
}

KEY = BaseConfig.SECRET_KEY
