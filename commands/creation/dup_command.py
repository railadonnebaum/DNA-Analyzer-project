try:
    from commands.creation.creation_commands import CreationCommand
    from dna.data_base import DataBase
    from dna.dna import Dna
except ImportError:
    print("Need to fix the installation")
    raise
'''
Dup Command.
command: dup <seq> [@<seq_name>]
seq might be a seq id: #id, or a seq name: #name.
if name is not provided a default name is set to be: original_name.
'''


class DupCommand(CreationCommand):

    def __init__(self, args):
        name, seq = self.parse(args)
        name = validate_name(name, seq)
        dna_sequence = self.get_sequence(seq)
        self.__dna = None
        if dna_sequence is not None:
            self.__dna = Dna(dna_sequence, name)

    def execute(self):
        if self.__dna is not None:
            self.print(Dna.get_id(), self.__dna.get_name(), self.__dna.get_dna_sequence())
            self.__dna.execute()


def validate_name(name, seq):
    data_base = DataBase()
    if name is None or data_base.name_exist(name[1:]) is not None:
        if seq[0] not in ['#', '@']:
            raise ValueError
        if seq[0] == '#':
            name = data_base.get_sequence_data_by_id(seq[1:])
        else:
            name = seq[1:]
        origin_name = name
        id = 1
        while data_base.name_exist(name) is not None:
            name = origin_name + '_' + str(id)
            id += 1
        return name
    if name[0] != '@':
        raise ValueError
    return name[1:]
