from abc import ABCMeta, abstractmethod


class ICubeA(metaclass=ABCMeta):
    width: int
    height: int
    depth: int
    
    @staticmethod
    @abstractmethod
    def manufacture(w, h, d):
        NotImplemented
