from chair_factory import ChairFactory
from table_factory import TableFactory
from interface_funiture import InterfaceFurniture

class FurnitureFactory(InterfaceFurniture):
    @staticmethod
    def get_furniture(furniture: str) ->InterfaceFurniture:
        "Static get_factory method"
        try:
            if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
                return ChairFactory.get_chair(furniture)
            if furniture in ['SmallTable', 'MediumTable', 'BigTable']:
                return TableFactory.get_table(furniture)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None