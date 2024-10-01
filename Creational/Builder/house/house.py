class House():
    "The Product"
    def __init__(self, building_type :str = "Apartment", doors :int = 0, windows: int=0, wall_material: str="Brick") -> None:
        self.building_type = ""
        self.doors = 0
        self.wall_material = ""
        self.windows = 0
    def construction(self) -> str:
        return f"This is a {self.wall_material} "\
            f"{self.building_type} with {self.doors} "\
            f"door(s) and {self.windows} window(s)."