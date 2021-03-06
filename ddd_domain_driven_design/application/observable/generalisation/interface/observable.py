"""Interface to create observable handler"""
from zope.interface import Interface
from typing import Union
from ....dto.generalisation.dto import DTO
from .observer import ObserverInterface


class ObservableInterface(Interface):
    """Interface to create observable handler"""

    def process(dto: Union[DTO, None]):
        """Processes with the given Command object"""

    def notify():
        """

        :return:
        """

    def attach(observer: ObserverInterface):
        """

        :return:
        """

    def detach(observer: ObserverInterface):
        """

        :return:
        """
