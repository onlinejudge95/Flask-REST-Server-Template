"""
Module to provide ping controller functionality
"""
from ..service import ping as service
from ..utils import decorators, dto
from flask_restplus import Resource


api = dto.PingDto.api


@api.route("/")
class Ping(Resource):
    @decorators.validate_headers
    @api.doc("ping")
    def get(self):
        """Ping response to find if the server is up"""
        return service.ping()
