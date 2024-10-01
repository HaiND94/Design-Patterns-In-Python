from house.house_builder import HouseBuilder

class IglooDirector:
    @staticmethod
    def construct():
        return HouseBuilder().set_building_type("Igloo").\
        set_wall_material("Ice").\
            set_number_windows(1).\
                set_number_doors(2).\
                    get_result()