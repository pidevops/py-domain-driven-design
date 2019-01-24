from zope.interface import implementer
from typing import Union
from ..dto.generalisation.dto import DTO
from .generalisation.interface.observable import ObservableInterface
from .generalisation.interface.observer import ObserverInterface


@implementer(ObservableInterface)
class Observable(object):
    """Adapter to create Command"""

    def __init__(self):
        self._observers = []
        self._dto = None

    @property
    def observers(self) -> dict:
        """
        observer objects

        :rtype: dict
        """

        return self._observers

    @property
    def dto(self) -> DTO:
        """
        dto object

        :rtype: DTO
        """
        return self._dto

    def process(self, dto: Union[DTO, None]):
        """Processes with the given Command object"""
        self._dto = dto
        self.notify()

    def notify(self):
        """

        :return:
        """
        for observer in self.observers:
            observer.update(self)

    def attach(self, observer: ObserverInterface):
        """

        :return:
        """
        self.observers.append(observer)

    def detach(self, observer: ObserverInterface):
        """

        :return:
        """
        self.observers.remove(observer)
