import functools
from flask import request

from .dto import PingDto

api = PingDto.api


def validate_headers(func):
    @functools.wraps(func)
    def check(*args, **kwargs):
        if request.headers.get("Content-Type") != "application/json":
            return api.abort(415)
        return func(*args, **kwargs)

    return check
