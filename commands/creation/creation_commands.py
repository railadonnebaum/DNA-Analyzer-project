try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
"""
CreationCommand Interface
"""


class CreationCommand:
    def __init__(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

    def parse(self, args):
        if len(args) > 1:
            name = args[1]
        else:
            name = None
        dna_sequence = args[0]
        return name, dna_sequence

    def get_sequence(self, seq):
        data_base = DataBase()
        if seq[0] not in ['#', '@']:
            raise ValueError
        if seq[0] == '#':
            return data_base.get_sequence_data_by_name(data_base.get_sequence_data_by_id(seq[1:]))
        else:
            return data_base.get_sequence_data_by_name(seq[1:])

    def print(self, id, name, sequence):
        print('[{}] {}: {}'.format(id, name, sequence))

    def validate_name(self, name, string):
        data_base = DataBase()
        if name is None or data_base.name_exist(name[1:]) is not None:
            if string == 'seq':
                name = string + str(self.get_id())
            else:
                name = string
            while data_base.name_exist(name) is not None:
                name = string + str(self.get_id())
                self.set_id(1)
            return name
        if name[0] != '@':
            raise ValueError
        return name[1:]



