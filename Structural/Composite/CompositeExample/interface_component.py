from abc import ABCMeta, abstractmethod

class IComponent(metaclass=ABCMeta):
    reference_to_parent = None
    
    @staticmethod
    @abstractmethod
    def dir(indent):
        NotImplemented
        
    @staticmethod
    @abstractmethod
    def detach():
        NotImplemented