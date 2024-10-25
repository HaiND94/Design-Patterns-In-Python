from abc import ABCMeta, abstractmethod


class ICubeB(metaclass=ABCMeta):
    top_left_front: list[int, int, int]
    bottom_right_back: list[int, int, int]
    
    @staticmethod
    @abstractmethod
    def create(tlf, brb):
        NotImplemented
