from abc import ABC, abstractmethod

class IHouse(ABC):
    @staticmethod
    @abstractmethod
    def set_building_type(type: int):
        NotImplemented
    
    @staticmethod
    @abstractmethod
    def set_wall_material(material: str):
        NotImplemented
    
    @staticmethod
    @abstractmethod
    def set_number_windows(number: int):
        NotImplemented
        
    @staticmethod
    @abstractmethod
    def set_number_doors(number: int):
        NotImplemented
    