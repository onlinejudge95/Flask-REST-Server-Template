"""
Configuration module for the app.
"""
import pathlib
import uuid


class BaseConfig:
    """
    Base configuration class to hold configuration settings as class variable.

    NOTE:- Never instantiate this class directly, the proper usage is to inherit
    from this class.

    >>> class CustomConfig(BaseConfig):
    ...    pass
    >>> app.config.from_object(CustomConfig())
    """
    TESTING = False
    BASE_DIR = pathlib.Path.cwd()
    SECRET_KEY = uuid.uuid4().hex


class DevelopmentConfig(BaseConfig):
    """
    Configuration class to hold configuration settings as class variables for
    development environment

    NOTE:- Proper usage is to instantiate this class directly.

    >>> dev_config = DevelopmentConfig()
    """
    JSONIFY_PRETTYPRINT_REGULAR = True


class TestingConfig(BaseConfig):
    """
    Configuration class to hold configuration settings as class variables for
    testing environment

    NOTE:- Proper usage is to instantiate this class directly.

    >>> test_config = TestingConfig()
    """
    TESTING = True
    JSONIFY_PRETTYPRINT_REGULAR = True


class ProductionConfig(BaseConfig):
    """
    Configuration class to hold configuration settings as class variables for
    production environment

    NOTE:- Proper usage is to instantiate this class directly.

    >>> prod_config = ProductionConfig()
    """
    JSONIFY_PRETTYPRINT_REGULAR = True


CFG_MAP = {
    "development": "app.src.config.DevelopmentConfig",
    "testing": "app.src.config.TestingConfig",
    "production": "app.src.config.ProductionConfig",
}

KEY = BaseConfig.SECRET_KEY
