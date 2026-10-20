"""
Subject module for the Observer pattern.
Defines the Subject abstract class that maintains a list of observers
"""
__author__ = "Kailine Lima"
__version__ = "1.0.0"

from abc import abstractmethod
from .observer import Observer

class Subject():
    """ Abstract class representing a subject in the observer pattern.
    """

    def __init__(self):
        """ Initialize the subject with an empty list of observers.
        """
        self._observers = []
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """ Attach an observer to the subject.

        Args:
            observer (Observer): The observer to attach.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """ Detach an observer from the subject.

        Args:
            observer (Observer): The observer to detach.
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """ Notify all attached observers of a change.
        """
        for observer in self._observers:
            observer.update(message)