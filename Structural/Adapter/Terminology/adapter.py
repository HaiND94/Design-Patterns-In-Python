from ia import IA
from b import B

class ClassBAdapter(IA):  
    def __init__(self):
        self.class_b = B()
        
    def method_a(self):
        "Call method b"
        self.class_b.method_b