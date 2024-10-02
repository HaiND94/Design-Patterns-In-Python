from table.interface_table import InterfaceTable
from table.big_table import BigTable
from table.small_table import SmallTable
from table.medium_table import MediumTable

class TableFactory:
    @staticmethod
    def get_table(table: str) -> InterfaceTable:
        try:
            if table == "BigTable":
                return BigTable()
            if table == "SmallTable":
                return SmallTable()
            if table == "MediumTable":
                return MediumTable()
            raise "Table not found"
        except Exception as _e:
            print(_e)
        return None