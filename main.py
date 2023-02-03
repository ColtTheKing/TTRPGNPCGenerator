import random

# the file is opened within the "with". it is closed after automatically
def get_list(file):
	with open(file) as f:
		lines = f.readlines()
		return [l.strip() for l in lines]

names_boys = get_list('names_boys.txt')
names_girls = get_list('names_girls.txt')
names_all = names_boys + names_girls
name_entry = names_all[random.randrange(len(names_all))]

occ = get_list('occupations.txt')
occ_entry = occ[random.randrange(len(occ))]

print(str(name_entry) + ", the " + str(occ_entry))

#print(stripped[random.randrange(len(ostripped))])