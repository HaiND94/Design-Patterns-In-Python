from interface_cube_b import ICubeB
import time

class CubeB(ICubeB):
    
    last_time = time.time()
    
    def create(self, top_left_front, bottom_right_back: list[int]):
        now = int(time.time())
        if now > int(CubeB.last_time + 2):
            CubeB.last_time = now
            return True
        return False