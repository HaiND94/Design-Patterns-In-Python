from house.house_builder import HouseBuilder

class CastleDirector:
    @staticmethod
    def construct():
        return HouseBuilder().set_building_type("castle").\
        set_wall_material("StandStone").\
            set_number_windows(100).\
                set_number_doors(100).\
                    get_result()