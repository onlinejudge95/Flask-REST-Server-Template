"""
Module to provide ping controller functionality
"""
from flask_restplus import Resource

from ..service import ping as service
from ..utils import decorators, dto

api = dto.PingDto.api


@api.route("/")
class Ping(Resource):
    @decorators.validate_headers
    @api.doc("ping")
    def get(self):
        """Ping response to find if the server is up"""
        return service.ping()
