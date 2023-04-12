import random
from abc import ABC, abstractmethod

supported_genders = ["masc", "femme", "neutral", "any"]

class TTRPGSystem(ABC):
    "Represents a tabletop system for the characters to be created within"

    # open the given file and put each line into an array
    def get_entries_from_file(self, file):
        # the file is opened within the "with". it is closed after automatically
        with open(file) as f:
            lines = f.readlines()
            return [
                l.strip() for l in lines
            ]  # take off the extra new line character from each line


    # returns a name of the desired gender
    def generate_name(self, gender):
        # load names from data files
        if gender == "masc":
            names = self.get_entries_from_file("names_boys.txt")
        elif gender == "femme":
            names = self.get_entries_from_file("names_girls.txt")
        else:  # SEPARATE THIS OUT ONCE WE HAVE A LIST OF GENDER NEUTRAL NAMES
            names = self.get_entries_from_file("names_boys.txt") + self.get_entries_from_file("names_girls.txt")

        # return a random name from the chosen list
        return names[random.randrange(len(names))]


    # returns a random occupation
    def generate_occupation(self):
        occupations = self.get_entries_from_file("occupations.txt")
        return occupations[random.randrange(len(occupations))]


    # returns a random quirk
    def generate_quirk(self):
        quirks = self.get_entries_from_file("quirks.txt")
        return quirks[random.randrange(len(quirks))]


    # generates the details of a single npc
    @abstractmethod
    def generate_npc(self, gender):
        pass


    # generates the details of the desired number of npcs
    def generate_npcs(self, number, gender):
        npc_list = []
        for i in range(number):
            npc_list.append(self.generate_npc(gender))
        return npc_list


class TTRPG_NPC(ABC):
    "Represents the NPCs themselves"

    def __init__(self, name_entry, occ_entry, quirk_entry):
        self.name_entry = name_entry
        self.occ_entry = occ_entry
        self.quirk_entry = quirk_entry


    @abstractmethod
    def print_npc(self):
        pass