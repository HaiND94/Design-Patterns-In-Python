from abc import ABC, abstractmethod

class InterfaceFurniture(ABC):
    @staticmethod
    @abstractmethod
    def get_furniture(type: str):
        NotImplemented