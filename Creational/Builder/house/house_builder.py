from .interface_house import IHouse
from .house import House

class HouseBuilder(IHouse):
    house: House
    def __init__(self) -> None:
        self.house = House()
    def set_building_type(self, building_type: str):
        self.house.building_type = building_type
        return self
    def set_wall_material(self, wall_material: str):
        self.house.wall_material = wall_material
        return self
    def set_number_doors(self, number: int):
        self.house.doors = number
        return self
    def set_number_windows(self, number: int):
        self.house.windows = number
        return self
    def get_result(self) -> House:
        return self.house