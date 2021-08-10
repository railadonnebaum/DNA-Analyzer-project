try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
"""
Management Commands Interface
"""


class ManagementCommands:
    def __init__(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

    def parse(self, type, args):
        if type == "del":
            dna_sequence = args[0]
            return dna_sequence
        if type == "save":
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

    def get_name(self, seq):
        data_base = DataBase()
        if seq[0] not in ['#', '@']:
            raise ValueError
        if seq[0] == '#':
            return data_base.get_sequence_data_by_id(seq[1:])
        else:
            return seq[1:]

    def get_id(self, seq):
        data_base = DataBase()
        if seq[0] == '#':
            return seq[1:]
        if seq[0] == '@':
            return data_base.get_id(seq[1:])
        raise ValueError
