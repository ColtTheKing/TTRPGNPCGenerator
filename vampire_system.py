import ttrpg_system


class VampireSystem(ttrpg_system.TTRPGSystem):
    "Represents the tabletop system of vampire the masquerade"

    # open the given file and put each line into an array
    def get_entries_from_file(self, file):
        ttrpg_system.TTRPGSystem.get_entries_from_file(self, file)


    # generate a name of the desired gender
    def generate_name(self, gender):
        ttrpg_system.TTRPGSystem.generate_name(self, gender)


    def generate_occupation(self):
        ttrpg_system.TTRPGSystem.generate_occupation(self)


    def generate_quirk(self):
        ttrpg_system.TTRPGSystem.generate_quirk(self)


    def generate_npcs(self, number, gender):
        ttrpg_system.TTRPGSystem.generate_npcs(self, number, gender)
