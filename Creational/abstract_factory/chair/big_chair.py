from .interface_chair import InterfaceChair

class BigChair(InterfaceChair):
    def __init__(self):
        self._height = 60
        self._width = 120
        self._depth = 80
    def get_dimensions(self):
        return {
            "with": self._width,
            "height": self._height,
            "depth": self._depth
        }
        