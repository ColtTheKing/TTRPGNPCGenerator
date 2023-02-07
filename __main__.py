import random
import argparse

def check_positive(value):
	int_value = int(value)
	if int_value < 1:
		raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
	return int_value

# initializing parser
parser = argparse.ArgumentParser(description ="An NPC Generator for TTRPGs",
	formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-s", "--system", default='V5', help="TTRPG System & Edition")
parser.add_argument("-n", "--number", default=1, type=check_positive, help="Number of names to generate")
args = vars(parser.parse_args())

# set up parameters
system = args['system'].lower()
number = args['number']

# the file is opened within the "with". it is closed after automatically
def get_list(file):
	with open(file) as f:
		lines = f.readlines()
		return [l.strip() for l in lines]



names_boys = get_list('names_boys.txt')
names_girls = get_list('names_girls.txt')
names_all = names_boys + names_girls


occ = get_list('occupations.txt')


# command line stuff practice

if system == 'v5':
	print('VAMPIRE: THE MASQUERADE')
if system == 'dnd' or system == 'd&d':
	print('DUNGEONS & DRAGONS')

for i in range(number):
	name_entry = names_all[random.randrange(len(names_all))]
	occ_entry = occ[random.randrange(len(occ))]
	print(str(name_entry) + ", the " + str(occ_entry))

#print(stripped[random.randrange(len(ostripped))])