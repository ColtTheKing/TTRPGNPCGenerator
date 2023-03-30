import ttrpg_system
import random


class VampireSystem(ttrpg_system.TTRPGSystem):
    "Represents the tabletop system of vampire the masquerade"

    def generate_clan():
        # decide bane as well in here prob
    def generate_attributes():
        # just an idea, very incomplete
        attributes = [4, 3, 3, 3, 2, 2, 2, 2, 1]
        random.shuffle(attributes)

