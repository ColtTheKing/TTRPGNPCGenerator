import random


class TTRPGSystem:
    "Represents a tabletop system for the characters to be created within"

    supported_genders = ["masc", "femme", "neutral", "any"]

    # open the given file and put each line into an array
    def get_entries_from_file(self, file):
        # the file is opened within the "with". it is closed after automatically
        with open(file) as f:
            lines = f.readlines()
            return [
                l.strip() for l in lines
            ]  # take off the extra new line character from each line

    # generate a name of the desired gender
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

    def generate_occupation(self):
        occupations = self.get_entries_from_file("occupations.txt")
        return occupations[random.randrange(len(occupations))]


    def generate_quirk(self):
        quirks = self.get_entries_from_file("quirks.txt")
        return quirks[random.randrange(len(quirks))]
    
    
    def generate_npcs(self, number, gender):
        for i in range(number):
            name_entry = self.generate_name(gender)
            occ_entry = self.generate_occupation()
            quirk_entry = self.generate_quirk()
            print(str(name_entry) + " the " + str(occ_entry) + ", " + str(quirk_entry) + ".")
    