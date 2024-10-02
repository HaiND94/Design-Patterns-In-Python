from interface_value import IValue

class Value(IValue):
    value: str
    
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)