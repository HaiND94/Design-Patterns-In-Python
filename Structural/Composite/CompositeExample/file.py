from interface_component import IComponent

class File(IComponent):
    
    def __init__(self, name: str):
        self.name = name
        
    def dir(self, indent):
        parent_id = (id(self.reference_to_parent)
                     if self.reference_to_parent is not None else None)
        print(
            f"{indent}<FILE> {self.name}\t\t"
            f"id:{id(self)}\tParent:\t{parent_id}"
        )
    
    def detach(self):
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)