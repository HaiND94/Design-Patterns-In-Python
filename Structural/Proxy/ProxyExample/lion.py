from interface_proteus import IProteus

import random
from interface_proteus import IProteus
import leopard
import serpent

class Lion(IProteus):
    "Proteus in the form of a Lion"

    name = "Lion"

    def tell_me_the_future(self):
        "Proteus will change to something random"
        self.__class__ = leopard.Leopard if random.randint(
            0, 1) else serpent.Serpent

    @classmethod
    def tell_me_your_from(cls):
        print("I am from of a " + cls.name)