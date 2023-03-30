import ttrpg_system
<<<<<<< HEAD
=======
import json
>>>>>>> a2a7e290853f191edf729f1e998eaa88ff662191
import random


class VampireSystem(ttrpg_system.TTRPGSystem):
    "Represents the tabletop system of vampire the masquerade"

<<<<<<< HEAD
=======
    # randomizes the given stat spread
    def randomize_stat_spread(self, stats):
        pass #WRITE THIS CODE


    # returns a random spread of attribute points
    def generate_attributes(self, attribute_data):
        attributes = attribute_data["names"]
        attribute_values = attribute_data["starting_spread"]
        self.randomize_stat_spread(attribute_values)

        attribute_output = "Attributes:"
        for i in len(attributes):
            if i % 3 == 0:
                attribute_output += "\n"
            attribute_output += attributes[i] + ": " + attribute_values[i] + ", "

        return attribute_output


    # returns a random spread of skill points
    def generate_skills(self, skill_data):
        skills = skill_data["names"]
        num_skill_spreads = len(skill_data["starting_spreads"])
        skill_values = skill_data["starting_spreads"][random.randrange(num_skill_spreads)]
        self.randomize_stat_spread(skill_values)

        skill_output = "Skills:"
        for i in len(skills):
            if i % 3 == 0:
                skill_output += "\n"
            skill_output += skills[i] + ": " + skill_values[i] + ", "

        return skill_output
            

    # returns a random spread of attribute and skill points
    def generate_stats(self):
        f = open('v5_data.json')
        data = json.load(f)

        self.generate_attributes(data["Attributes"])
        self.generate_skills(data["Skills"])
>>>>>>> a2a7e290853f191edf729f1e998eaa88ff662191

