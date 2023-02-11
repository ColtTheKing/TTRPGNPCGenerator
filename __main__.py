import random
import argparse
import ttrpg_system
import vampire_system

supported_systems = ["v5", "dnd", "d&d"]
supported_genders = ["masc", "femme", "neutral", "any"]

ttrpg_system = None

# ensure the requested system is a supported ttrpg system, throw an error if it isn't
def check_valid_system(system):
    if not system.lower() in supported_systems:
        s_systems = ", ".join(supported_systems)
        raise argparse.ArgumentTypeError(
            "%s is not a supported ttrpg system. Supported systems are %s"
            % (system, s_systems)
        )
    return system


# ensure the number of entries requested is positive, throw an error if it isn't
def check_valid_number(number):
    int_value = int(number)
    if int_value < 1:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % number)
    return int_value


# ensure the requested gender is a supported gender, throw an error if it isn't
def check_valid_gender(gender):
    if not gender.lower() in supported_genders:
        s_genders = ", ".join(supported_genders)
        raise argparse.ArgumentTypeError(
            "%s is not a supported gender. Supported genders are %s"
            % (gender, s_genders)
        )
    return gender


# open the given file and put each line into an array
def get_entries_from_file(file):
    # the file is opened within the "with". it is closed after automatically
    with open(file) as f:
        lines = f.readlines()
        return [
            l.strip() for l in lines
        ]  # take off the extra new line character from each line


# run the program with vampire the masquerade as the system used for NPC generation
def run_as_vampire():
    ttrpg_system = ttrpg_system.VampireSystem()


# run the program with dungeons & dragons as the system used for NPC generation
def run_as_dnd():
    ttrpg_system = ttrpg_system.DnDSystem()


# initializing argument parser
parser = argparse.ArgumentParser(
    description="An NPC Generator for TTRPGs",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
# determines which ttrpg system the characters are for
parser.add_argument(
    "-s",
    "--system",
    default="V5",
    type=check_valid_system,
    help="TTRPG System & Edition (v5, dnd)",
)

# put the arguments in a dictionary so they can be accessed later
args = vars(parser.parse_args())

# storing the input arguments to use later
system = args["system"].lower()

# print the full name of the ttrpg system
if system == "v5":
    run_as_vampire()
elif system == "dnd" or system == "d&d":
    run_as_dnd()


# prompt user for NPCS
while True:
    # maybe have one prompt for what action to take (ex. generate_npc, upload_names, change_settings)

    user_input = input("Enter the parameters for NPC generation: ").lower()

    if user_input == "quit":
        break

    # MAKE SUBPARSERS, ONE OF WHICH IS FOR NPC GENERATION
    # MAYBE DIFFERENT SUBPARSER FOR EACH SYSTEM
    # MAKE SETTINGS FILE THAT HOLDS FILENAMES FOR NAMES, ETC
    # SETTINGS CAN BE CHANGED BY COMMANDS WITH OTHER SUBPARSERS LIKE CHANGE_NAME_FILE

    # -number 5 -gender any etc.

    # for i in range(number):
    #    name_entry = generate_name(gender)
    #    occ_entry = generate_occupation()
    #    quirk_entry = generate_quirk()
    #    print(
    #        str(name_entry) + ", the " + str(occ_entry) + ", " + str(quirk_entry) + "."
    #    )


# -----------------------------------------------------------------------------------------

# determines how many characters to generate
# parser.add_argument(
#    "-n",
#    "--number",
#    default=1,
#    type=check_valid_number,
#    help="Number of names to generate",
# )
# determines the gender of the character
# parser.add_argument(
#    "-g",
#    "--gender",
#    default="any",
#    type=check_valid_gender,
#    help="Gender of the character (masc, femme, neutral, any)",
# )
