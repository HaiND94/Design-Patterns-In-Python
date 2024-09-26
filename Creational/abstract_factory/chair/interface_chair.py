from abc import ABC, abstractmethod

class InterfaceChair(ABC):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        pass