from abc import ABC, abstractmethod


class IA(ABC):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def method_a():
        NotImplemented