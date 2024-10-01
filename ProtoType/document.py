from interface_prototype import IDocument
import copy

class Document(IDocument):
    # name: str
    # arr: list
    def __init__(self, name: str, arr: list) -> None:
        self.name = name
        self.arr = arr
        
    def clone(self, mode: int):
        if mode == 1:
            doc_arr = self.arr
        if mode == 2:
            doc_arr = self.arr.copy()
        if mode == 3:
            doc_arr = copy.deepcopy(self.arr)
        return type(self) (
            self.name,
            doc_arr
        )
    def __str__(self):
        " Overriding the default __str__ method for our object."
        return f"{id(self)}\tname={self.name}\tlist={self.arr}"
