"""
Module to register our Blueprints
"""
from flask import Blueprint
from flask_restplus import Api

from .src.controller.ping import api as ping_ns

blueprint = Blueprint("api", __name__) # pylint: disable=invalid-name

# pylint: disable=invalid-name
api = Api(
    blueprint,
    title="Flask-RESTplus API server",
    version="1.0.0",
    description="REST server for py",
)

api.add_namespace(ping_ns, path="/ping")
