import argparse
import ttrpg_system
import vampire_system
import dnd_system

supported_systems = ["v5", "vampire", "dnd", "d&d"]

current_system = None


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
    if not gender.lower() in ttrpg_system.TTRPGSystem.supported_genders:
        s_genders = ", ".join(ttrpg_system.TTRPGSystem.supported_genders)
        raise argparse.ArgumentTypeError(
            "%s is not a supported gender. Supported genders are %s"
            % (gender, s_genders)
        )
    return gender


# run the program with vampire the masquerade as the system used for NPC generation
def run_as_vampire(number, gender):
    current_system = vampire_system.VampireSystem()
    print(current_system.generate_npcs(number, gender))


# run the program with dungeons & dragons as the system used for NPC generation
def run_as_dnd(number, gender):
    current_system = dnd_system.DnDSystem()
    print(current_system.generate_npcs(number, gender))

    # create parsers and subparsers for user to input commands
def setup_parsers():
    # initializing argument parser
    parser = argparse.ArgumentParser(
        description="An NPC Generator for TTRPGs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # add an argument to determine which ttrpg system the characters are for
    parser.add_argument(
        "-s",
        "--system",
        default="v5",
        type=check_valid_system,
        help="TTRPG System & Edition (v5, dnd)",
    )

    # add an argument to determine how many characters to generate
    parser.add_argument(
        "-n",
        "--number",
        default=1,
        type=check_valid_number,
        help="Number of npcs to generate",
    )

    # add an argument to determine the gender of the character
    parser.add_argument(
        "-g",
        "--gender",
        default="any",
        type=check_valid_gender,
        help="Gender of the character (masc, femme, neutral, any)",
    )

    # THIS WILL BE USED LATER
    # add subparsers for various settings commands such as switching data files, formatting, etc.
    # subparsers = parser.add_subparsers(help="Placeholder subparser help")

    # create the parser for the "settings" command
    # parser_settings = subparsers.add_parser("settings", help="Allows changing of generation settings")
    # parser_settings.add_argument("-n", "--name", help="Enter the name of the setting to change, then the value to insert")

    return parser


# ==================== PROGRAM ENTRY POINT ====================

# initializing argument parser
parser = setup_parsers()

# put the argument values given by the user in a dictionary so they can be accessed later
args = vars(parser.parse_args())

# use the arguments to determine which system to run and what parameters to use
system = args["system"].lower()
number = args['number']
gender = args['gender']

if system == "v5" or system == "vampire":
    run_as_vampire(number, gender)
elif system == "dnd" or system == "d&d":
    run_as_dnd(number, gender)
