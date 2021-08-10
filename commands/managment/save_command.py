try:
    from commands.managment.management_commands import ManagementCommands
except ImportError:
    print("Need to fix the installation")
    raise
'''
Save Command.
command: save <seq> [<file_name>]
seq might be a seq id: #id, or a seq name: #name.
if the file name is not provided, the sequence name is being used.
'''


class SaveCommand(ManagementCommands):
    def __init__(self, args):
        self.__sequence = self.get_sequence(args[0])
        if len(args) > 1:
            self.__file = args[1] + '.rawdna'
        else:
            self.__file = self.get_name(args[0]) + '.rawdna'

    def execute(self):
        with open('resources/' + self.__file, 'w') as write_file:
            write_file.write(str(self.__sequence))
            print("Saved Dna_sequence: {}".format(self.__sequence))
