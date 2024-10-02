from abc import ABC, abstractmethod

class InterfaceTable(ABC):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        NotImplemented