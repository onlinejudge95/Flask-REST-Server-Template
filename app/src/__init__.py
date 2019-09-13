"""
App factory for our server.
"""
from .config import config_map
from dotenv import find_dotenv, load_dotenv
from flask import Flask

import os
import pathlib


load_dotenv(dotenv_path=str(pathlib.Path.cwd() / ".env"), verbose=True)


def create_app(cfg):
    app = Flask(__name__)
    app.config.from_object(config_map[cfg])

    return app
