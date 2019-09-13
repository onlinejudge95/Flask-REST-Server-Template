"Module to implement ping data objects"
from flask_restplus import Namespace, fields


class PingDto:
    api = Namespace("ping", description="ping related operations")
