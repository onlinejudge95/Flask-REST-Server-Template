"""
App factory for our server.
"""
import os
import pathlib

from dotenv import load_dotenv
from flask import Flask

from app.src.config import CFG_MAP


load_dotenv(dotenv_path=str(pathlib.Path.cwd() / ".env"), verbose=True)


def create_app(cfg):
    """
    App factory to create app instance with provided environment settings.

    The following creates an app instance for different environments
    >>> production_app = create_app("production")
    >>> development_app = create_app("development")
    >>> testing_app = create_app("testing")

    :param: cfg
    Configuration to setup the corresponding environment.
    """
    app = Flask(__name__)
    app.config.from_object(CFG_MAP[cfg])

    return app
