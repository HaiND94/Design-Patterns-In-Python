from abc import ABCMeta, abstractmethod

class IB(metaclass=ABCMeta):
    "This is an interface"
    @staticmethod
    @abstractmethod
    def method_b(self):
        "this is method b"
        