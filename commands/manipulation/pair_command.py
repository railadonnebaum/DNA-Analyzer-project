try:
    from commands.manipulation.manipulation_commands import ManipulationCommands
    from dna.data_base import DataBase
    from dna.dna import Dna
except ImportError:
    print("Need to fix the installation")
    raise
'''
Pair Command.
command: pair <seq> [: @<new_name> | @@]
seq might be a seq id: #id, or a seq name: #name.
if name is not provided a the pair command changes the original seq, if @@ is provided,
a default name is set to be <original_name_p1>
'''


class PairCommand(ManipulationCommands):
    def __init__(self, args):
        data_base = DataBase()
        dna_id, new_name = self.parse(args)
        self.__name = self.get_name(dna_id)
        self.__dna_sequence = self.get_sequence(dna_id)
        self.__id = self.get_id(dna_id)
        self.__dna = None
        if new_name is not None:
            self.__name = self.get_new_name(self.__name, new_name, 'p')
            self.__dna_sequence = replace_seq(self.__dna_sequence)
            self.__dna = Dna(self.__dna_sequence, self.__name)
        else:
            self.__dna_sequence = replace_seq(self.__dna_sequence)
            data_base.set_sequence_data_by_name(self.__name, self.__dna_sequence)

    def execute(self):
        if self.__dna:
            self.print(Dna.get_id(), self.__name, self.__dna_sequence)
            self.__dna.execute()
        else:
            self.print(self.__id, self.__name, self.__dna_sequence)


def replace_seq(seq):
    new_dna_sequence = str(seq)
    new_dna_sequence = new_dna_sequence.replace('A', '!')
    new_dna_sequence = new_dna_sequence.replace('T', 'A')
    new_dna_sequence = new_dna_sequence.replace('!', 'T')
    new_dna_sequence = new_dna_sequence.replace('C', '!')
    new_dna_sequence = new_dna_sequence.replace('G', 'C')
    new_dna_sequence = new_dna_sequence.replace('!', 'G')
    return new_dna_sequence
