class TTRPGSystem:
    "Represents a tabletop system for the characters to be created within"

    def __init__():

    # generate a name of the desired gender
    def generate_name(gender):
        # load names from data files
        if gender == "masc":
            names = get_entries_from_file("names_boys.txt")
        elif gender == "femme":
            names = get_entries_from_file("names_girls.txt")
        else:  # SEPARATE THIS OUT ONCE WE HAVE A LIST OF GENDER NEUTRAL NAMES
            names = get_entries_from_file("names_boys.txt") + get_entries_from_file("names_girls.txt")

        # return a random name from the chosen list
        return names[random.randrange(len(names))]  

    def generate_occupation():
        occupations = get_entries_from_file("occupations.txt")
        return occupations[random.randrange(len(occupations))]


    def generate_quirk():
        quirks = get_entries_from_file("quirks.txt")
        return quirks[random.randrange(len(quirks))]