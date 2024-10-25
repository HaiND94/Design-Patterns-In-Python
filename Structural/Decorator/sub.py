from interface_value import IValue

class Sub(IValue):
    def __init__(self, val1: IValue, val2: IValue) -> None:
        val1 = getattr(val1, 'value', val1)
        val2 = getattr(val2, 'value', val2)
        self.value = val1 - val2
    def __str__(self) -> str:
        return str(self.value)