from interface_value import IValue

class Add(IValue):
    
    def __init__(self, val1: float, val2: float) -> None:
        self.value = val1 + val2
        
    def __str__(self) -> str:
        return str(self.value)
    