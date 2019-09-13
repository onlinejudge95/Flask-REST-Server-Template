"""
Module to register our Blueprints
"""
from .src.controller.ping import api as ping_ns
from flask import Blueprint
from flask_restplus import Api


blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Flask-RESTplus API server",
    version="1.0.0",
    description="REST server for py",
)

api.add_namespace(ping_ns, path="/ping")
