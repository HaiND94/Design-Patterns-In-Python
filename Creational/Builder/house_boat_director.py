from house.house_builder import HouseBuilder

class HouseBoatDirector:
    @staticmethod
    def construct():
        return HouseBuilder().set_building_type("House Boat").\
        set_wall_material("Wood").\
            set_number_windows(6).\
                set_number_doors(8).\
                    get_result()