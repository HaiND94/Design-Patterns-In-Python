import copy

class Singleton():
    "The Singleton Class"
    values = []
    
    def __new__(cls):
        return cls
    
    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"
    
    @staticmethod
    def class_method(cls):
        "Use @classmethod to access class level variables"
        print(cls.values)

# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")


