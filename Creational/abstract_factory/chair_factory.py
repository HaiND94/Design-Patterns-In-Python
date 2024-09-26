from chair.small_chair import SmallChair
from chair.big_chair import BigChair
from chair.medium_chair import MediumChair
from chair.interface_chair import InterfaceChair

class ChairFactory:
    @staticmethod
    def get_chair(chair: str) -> InterfaceChair:
        try:
            if chair == "SmallChair":
                return SmallChair()
            if chair == "BigChair":
                return BigChair()
            if chair == "MediumChair":
                return MediumChair()
            raise Exception('Chair Not Found')
        except Exception as _e:
            print(_e)
        return None
    
            
            