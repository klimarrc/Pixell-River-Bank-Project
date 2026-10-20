"""
Observer module for the Observer pattern.
Defines the Observer abstract class that gets notified by the Subject.     
"""
___author__ = "Kailine Lima"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """ Abstract class representing an observer in the observer pattern.
    """

    @abstractmethod
    def update(self, subject: object) -> None:
        """ Update the observer with information from the subject.

        Args:
            subject (object): The subject that notifies the observer.
        """
        pass