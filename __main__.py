import random
import argparse

supported_systems = ['v5', 'dnd', 'd&d']
supported_genders = ['male', 'female', 'neutral', 'any']

# ensure the requested system is a supported ttrpg system, throw an error if it isn't
def check_valid_system(system):
    if (not system.lower() in supported_systems):
        s_systems = ', '.join(supported_systems)
        raise argparse.ArgumentTypeError("%s is not a supported ttrpg system. Supported systems are %s" % (system, s_systems))
    return system

# ensure the number of entries requested is positive, throw an error if it isn't
def check_valid_number(number):
    int_value = int(number)
    if (int_value < 1):
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % number)
    return int_value

# ensure the requested gender is a supported gender, throw an error if it isn't
def check_valid_gender(gender):
    if (not gender.lower() in supported_genders):
        s_genders = ', '.join(supported_genders)
        raise argparse.ArgumentTypeError("%s is not a supported gender. Supported genders are %s" % (gender, s_genders))
    return gender
    
# open the given file and put each line into an array
def get_entries_from_file(file):
    # the file is opened within the "with". it is closed after automatically
    with open(file) as f:
        lines = f.readlines()
        return [l.strip() for l in lines] # take off the extra new line character from each line
        
# generate a name of the desired gender
def generate_name(gender):
    # load names from data files
    if (gender == 'male'):
        names = get_entries_from_file('names_boys.txt')
    elif (gender == 'female'):
        names = get_entries_from_file('names_girls.txt')
    else: # SEPARATE THIS OUT ONCE WE HAVE A LIST OF GENDER NEUTRAL NAMES
        names = get_entries_from_file('names_boys.txt') + get_entries_from_file('names_girls.txt')
    return names[random.randrange(len(names))] # return a random name from the chosen list

def generate_occupation():
    occupations = get_entries_from_file('occupations.txt')
    return occupations[random.randrange(len(occupations))]

def generate_quirk():
    quirks = get_entries_from_file('quirks.txt')
    return quirks[random.randrange(len(quirks))]


# initializing argument parser
parser = argparse.ArgumentParser(description ="An NPC Generator for TTRPGs",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# determines which ttrpg system the characters are for
parser.add_argument("-s", "--system", default='V5', type=check_valid_system, help="TTRPG System & Edition (v5, dnd)")
# determines how many characters to generate
parser.add_argument("-n", "--number", default=1, type=check_valid_number, help="Number of names to generate")
# determines the gender of the character
parser.add_argument("-g", "--gender", default='any', type=check_valid_gender, help="Gender of the character (male, female, neutral, any)")
# put the arguments in a dictionary so they can be accessed later
args = vars(parser.parse_args())

# storing the input arguments to use later
system = args['system'].lower()
number = args['number']
gender = args['gender']

# print the full name of the ttrpg system
if (system == 'v5'):
    print('VAMPIRE: THE MASQUERADE')
elif (system == 'dnd' or system == 'd&d'):
    print('DUNGEONS & DRAGONS')

# print the desired number of npcs
for i in range(number):
    name_entry = generate_name(gender)
    occ_entry = generate_occupation()
    quirk_entry = generate_quirk()
    print(str(name_entry) + ", the " + str(occ_entry) + ", " + str(quirk_entry) + ".")
