from .interface_table import InterfaceTable

class MediumTable(InterfaceTable):
    def __init__(self):
        self._height = 60
        self._width = 110
        self._depth = 70
    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }