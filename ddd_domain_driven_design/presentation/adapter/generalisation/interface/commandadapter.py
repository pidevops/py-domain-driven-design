"""Define Command interface for adapter"""
from zope.interface import Interface
from ....request.generalisation.interface.request import RequestInterface


class CommandAdapterInterface(Interface):
    """Interface adapter to create Command"""

    def create_command_from_request(request: RequestInterface):
        """Create command with json string data given from request"""
