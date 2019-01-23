"""Exceptions"""


class BaseError(Exception):
    """
    BaseError Exception
    All exceptions define in project module need to inherit this Error class
    """
    def __init__(self, message):
        self.message = message
        super().__init__()
