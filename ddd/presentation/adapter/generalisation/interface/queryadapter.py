"""Define Query interface for adapter"""
from zope.interface import Interface
from ddd.presentation.request.generalisation.interface.request import RequestInterface


class QueryAdapterInterface(Interface):
    """Interface adapter to create Command"""

    def create_query_from_request(request: RequestInterface):
        """Create query with json string data given from request"""
