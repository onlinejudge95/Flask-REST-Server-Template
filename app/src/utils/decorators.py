from .dto import PingDto
from flask import request

import functools


api = PingDto.api


def validate_headers(func):
    @functools.wraps(func)
    def check(*args, **kwargs):
        if request.headers.get("Content-Type") != "application/json":
            return api.abort(415)
        return func(*args, **kwargs)

    return check
