"""Define backend interface for backend adapters"""
from zope.interface import Interface


class RequestInterface(Interface):
    """Interface to create json string data from args"""

    def get_request_parameters():
        """Create json string data from args"""
