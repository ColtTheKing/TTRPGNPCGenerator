import ttrpg_system
import json
import random


class VampireSystem(ttrpg_system.TTRPGSystem):
    "Represents the tabletop system of vampire the masquerade"

    # randomizes the given stat spread
    def randomize_stat_spread(self, stats):
        random.shuffle(stats)  


    # returns a random spread of attribute points
    def generate_attributes(self, attribute_data):
        attributes = attribute_data["names"]
        attribute_values = attribute_data["starting_spread"]
        self.randomize_stat_spread(attribute_values)

        attribute_output = "Attributes:"
        for i in range(len(attributes)):
            if i % 3 == 0:
                attribute_output += "\n"
            attribute_output += attributes[i] + ": " + str(attribute_values[i]) + ", "

        return attribute_output


    # returns a random spread of skill points
    def generate_skills(self, skill_data):
        skills = skill_data["names"]
        num_skill_spreads = len(skill_data["starting_spreads"])
        skill_values = skill_data["starting_spreads"][random.randrange(num_skill_spreads)]
        self.randomize_stat_spread(skill_values)

        skill_output = "Skills:"
        for i in range(len(skills)):
            if i % 3 == 0:
                skill_output += "\n"
            skill_output += skills[i] + ": " + str(skill_values[i]) + ", "

        return skill_output
            

    # returns a random spread of attribute and skill points
    def generate_stats(self):
        f = open('v5_data.json')
        data = json.load(f)

        attributes = self.generate_attributes(data["Attributes"])
        skills = self.generate_skills(data["Skills"])

        return attributes + "\n" + skills
    
    def generate_class(self):
        pass

    # this isnt done. please work on it
    # we need to make default npc class in ttrpg_system
    # then we need to make the vampire npc class in this file
    # then we need to make the other functions put data into npcs
    # then we need to make the print_npc function so we can have output
    def print_npc(self, npc):
        npc_details = npc.name_entry + " the " + npc.occ_entry + ", " + npc.quirk_entry + "."

        for i in range(len(self.attributes)):
            if i % 3 == 0:
                attribute_output += "\n"
            attribute_output += self.attributes[i] + ": " + str(npc.attribute_values[i]) + ", "

        for i in range(len(self.skills)):
            if i % 3 == 0:
                skill_output += "\n"
            skill_output += self.skills[i] + ": " + str(npc.skill_values[i]) + ", "

        npc_details += "\nATTRIBUTES:" + attribute_output + "\nSKILLS:" + skill_output
