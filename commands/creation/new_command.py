try:
    from commands.creation.creation_commands import CreationCommand
    from dna.dna import Dna
    from dna.dna_sequence import DnaSequence
except ImportError:
    print("Need to fix the installation")
    raise
'''
New Command.
command: new <seq> [@<seq_name>]
if name is not provided a default name is set to be: seq.
'''


class NewCommand(CreationCommand):
    __id = 1

    def __init__(self, args):
        name, dna_sequence = self.parse(args)
        self.__name = self.validate_name(name, 'seq')
        self.__dna_sequence = DnaSequence(dna_sequence)
        self.__dna = Dna(dna_sequence, self.__name)

    def execute(self):
        self.print(Dna.get_id(), self.__dna.get_name(), self.__dna_sequence)
        self.__dna.execute()

    @staticmethod
    def get_id():
        return NewCommand.__id

    @staticmethod
    def set_id(id):
        NewCommand.__id += id
