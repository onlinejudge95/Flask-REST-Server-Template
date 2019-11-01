"""
Module to register our Blueprints
"""
from flask import Blueprint
from flask_restplus import Api

from app.src.controller import ping

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Flask-RESTplus API server",
    version="1.1.0",
    description="REST server template written in Flask",
)

api.add_namespace(ping.api, path="/ping")
