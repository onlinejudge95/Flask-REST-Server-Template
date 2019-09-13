"""
Module to provide ping service fundtionality
"""


def ping():
    response_object = {"status": "success", "message": "PONG"}
    return (response_object, 200, {"Connection": "close"})
