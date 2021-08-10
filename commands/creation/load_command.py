try:
    from commands.creation.creation_commands import CreationCommand
    from dna.dna import Dna
    from dna.dna_sequence import DnaSequence
except ImportError:
    print("Need to fix the installation")
    raise
'''
Load Command.
command: load <filename.rawdna> [@<seq_name>]
if name is not provided a default name is set to be: filename.
'''


class LoadCommand(CreationCommand):
    __id = 1

    def __init__(self, args):
        name, file = self.parse(args)
        name = self.validate_name(name, file.split('.')[0])
        self.__dna_sequence = DnaSequence(get_sequence(file))
        self.__dna = Dna(self.__dna_sequence, name)

    def execute(self):
        seq = self.__dna.get_dna_sequence()
        if len(seq) > 40:
            seq = seq[:33] + '...' + seq[-3:]
        self.print(Dna.get_id(), self.__dna.get_name(), seq)
        self.__dna.execute()

    @staticmethod
    def get_id():
        return LoadCommand.__id

    @staticmethod
    def set_id(id):
        LoadCommand.__id += id


def get_sequence(file):
    with open('resources/' + file, 'r') as load_file:
        sequence = load_file.read()
        return sequence
