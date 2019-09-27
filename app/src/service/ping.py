"""
Module to provide ping service funcssstionality
"""


def ping():
    """
    Ping service, it basically checks if the server is up or not.
    >>> obj = ping()
    >>> obj.response
    >>> {"status": "success", "message": "PONG"}
    >>> obj.status_code
    >>> 200
    """
    response_object = {"status": "success", "message": "PONG"}
    return response_object, 200
