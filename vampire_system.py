import ttrpg_system
import json
import random

attribute_names = None
skill_names = None


class VampireSystem(ttrpg_system.TTRPGSystem):
    "Represents the tabletop system of vampire the masquerade"

    def __init__(self):
        f = open("v5_data.json")
        self.json_data = json.load(f)

        global attribute_names, skill_names
        attribute_names = self.json_data["Attributes"]["names"]
        skill_names = self.json_data["Skills"]["names"]

    # returns a random spread of attribute points
    def generate_attributes(self):
        attribute_values = self.json_data["Attributes"]["starting_spread"]
        random.shuffle(attribute_values)
        return attribute_values

    # returns a random spread of skill points
    def generate_skills(self):
        num_skill_spreads = len(self.json_data["Skills"]["starting_spreads"])
        skill_values = self.json_data["Skills"]["starting_spreads"][
            random.randrange(num_skill_spreads)
        ]
        random.shuffle(skill_values)
        return skill_values

    def generate_npc(self, gender):
        name_entry = self.generate_name(gender)
        occ_entry = self.generate_occupation()
        quirk_entry = self.generate_quirk()
        attribute_entry = self.generate_attributes()
        skill_entry = self.generate_skills()

        return Vampire_NPC(
            name_entry, occ_entry, quirk_entry, attribute_entry, skill_entry
        )


class Vampire_NPC(ttrpg_system.TTRPG_NPC):
    "Represents the NPCs themselves within vampire the masquerade"

    def __init__(
        self, name_entry, occ_entry, quirk_entry, attribute_entry, skill_entry
    ):
        super().__init__(name_entry, occ_entry, quirk_entry)
        self.attribute_entry = attribute_entry
        self.skill_entry = skill_entry

    def print_npc(self):
        npc_details = str(self.name_entry) + ", the " + str(self.occ_entry)
        npc_details += ", " + str(self.quirk_entry) + "."
        npc_details += "\n" + self.stats_to_text()
        print(npc_details)

    def stats_to_text(self):
        stat_text = "==========================ATTRIBUTES=========================="
        stat_text += self.attributes_to_text() + "\n"
        stat_text += "============================SKILLS============================"
        stat_text += self.skills_to_text()

        return stat_text

    def attributes_to_text(self):
        attribute_output = ""
        for i in range(len(self.attribute_entry)):
            if i % 3 == 0:
                attribute_output += "\n"

            attribute_name = attribute_names[i] + ":"
            attribute_output += f"{attribute_name : <15}"
            attribute_output += str(self.attribute_entry[i])

            if i % 3 != 2:
                attribute_output += "   |   "

        return attribute_output

    def skills_to_text(self):
        skill_output = ""
        for i in range(len(self.skill_entry)):
            if i % 3 == 0:
                skill_output += "\n"

            skill_name = skill_names[i] + ":"
            skill_output += f"{skill_name : <15}"
            skill_output += str(self.skill_entry[i])

            if i % 3 != 2:
                skill_output += "   |   "

        return skill_output
