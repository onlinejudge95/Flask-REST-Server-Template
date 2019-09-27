"""
Module to implement ping data objects
"""
from flask_restplus import Namespace


class PingDto:  # pylint: disable=too-few-public-methods
    """
    DTO object to operate in ping namespace.

    Use property `api` as blueprint in app.src.controller.ping.PingAPI
    """
    api = Namespace("ping", description="ping related operations")
