from abc import abstractmethod, ABCMeta

class IDocument(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def clone(mode):
        NotImplemented
    
    