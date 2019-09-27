"""
Module to provide ping controller functionality
"""
from flask_restplus import Resource

from ..service import ping as service
from ..utils import decorators, dto


api = dto.PingDto.api  # pylint: disable=invalid-name


@api.route("/")
class PingAPI(Resource):
    """
    Ping controller class.
    It handles the ping operation routing.
    This class subclasses flask_restplus.Resource, representing a
    resource for which all HTTP verbs are allowed as methods to operate on.

    This class receives the request from the server and calls the ping service on it.
    Endpoints defined are

    1. GET /ping/
    """
    @decorators.validate_headers
    @api.doc("ping")
    def get(self):  # pylint: disable=no-self-use
        """Ping response to find if the server is up"""
        return service.ping()
