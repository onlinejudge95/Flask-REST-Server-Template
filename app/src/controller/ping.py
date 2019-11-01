"""
Module to provide ping controller functionality
"""
from flask_restplus import Resource

from app.src.service import ping as service
from app.src.utils import serializer


api = serializer.AppSerializer.ping_api


@api.route("/")
class PingView(Resource):
    """
    Ping controller class.
    It handles the ping operation routing.
    This class subclasses flask_restplus.Resource, representing a
    resource for which all HTTP verbs are allowed as methods to operate on.

    This class receives the request from the server and calls the ping service on it.
    Endpoints defined are

    1. GET /ping/
    """
    @staticmethod
    @api.doc("ping")
    def get():
        """Ping response to find if the server is up"""
        return service.ping()
