from abc import abstractmethod, ABC


class IProteus(ABC):
    @staticmethod
    @abstractmethod
    def tell_me_the_future() -> None:
        NotImplemented
        
    @staticmethod
    @abstractmethod
    def tell_me_your_from() -> None:
        NotImplemented