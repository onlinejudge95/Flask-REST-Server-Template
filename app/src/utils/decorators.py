"""
Module for implementing custom decorators to extend function behaviour.

Usage:-

@decorator
def function(*args, **kwargs):
    pass
"""
import functools


def validate_headers(func):
    """
    Decorator to validate any header

    Currently it is left blank, we can implement following checks.
    * Content-Type check
    * Authorization check etc.
    """
    @functools.wraps(func)
    def check(*args, **kwargs):
        return func(*args, **kwargs)

    return check
