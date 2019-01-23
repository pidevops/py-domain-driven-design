from zope.interface import implementer
from ddd.presentation.request.generalisation.interface.request import RequestInterface
from ddd.presentation.adapter.generalisation.interface.commandadapter import CommandAdapterInterface
from ddd.application.dto.generalisation.dto import DTO


@implementer(CommandAdapterInterface)
class CommandAdapter(object):
    """Adapter to create Command"""

    def __init__(self, command: DTO):
        self.command = command

    def create_command_from_request(self, request: RequestInterface):
        """Create command with json string data given from request"""

        json_string = request.get_request_parameters()

        return self.command.from_json(json_string)
