from castle_director import CastleDirector
from igloo_director import IglooDirector
from house_boat_director import HouseBoatDirector

IGLOO = IglooDirector.construct()
CASTLE = CastleDirector.construct()
HOUSEBOAT = HouseBoatDirector.construct()

print(IGLOO.construction())
print(CASTLE.construction())
print(HOUSEBOAT.construction())