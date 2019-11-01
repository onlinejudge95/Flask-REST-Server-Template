"""
Module to implement ping data objects
"""
from flask_restplus import Namespace


class AppSerializer:
    """
    Serializer for server
    """
    ping_api = Namespace("ping", description="ping related operations")
