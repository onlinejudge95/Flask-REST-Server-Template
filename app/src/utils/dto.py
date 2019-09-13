"Module to implement ping data objects"
from flask_restplus import fields, Namespace


class PingDto:
    api = Namespace("ping", description="ping related operations")
