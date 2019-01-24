"""Interface to create observer handler"""
from zope.interface import Interface


class ObserverInterface(Interface):
    """Interface to create observer handler"""

    def update(subject):
        """
        Receive update from subject
        :return:
        """
