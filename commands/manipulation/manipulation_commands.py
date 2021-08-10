try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
"""
Manipulation Commands Interface
"""


class ManipulationCommands:
    def __init__(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

    def parse(self, args):
        dna_sequence = args[0]
        if len(args) > 2:
            if args[1] != ':':
                start_index = args[1]
                end_index = args[2]
                if len(args) > 3:
                    if args[3] != ':':
                        raise ValueError
                    new_name = args[4]
                else:
                    new_name = None
                return dna_sequence, start_index, end_index, new_name
            else:
                new_name = args[2]
        else:
            new_name = None
        return dna_sequence, new_name

    def get_name(self, seq):
        data_base = DataBase()
        if seq[0] not in ['#', '@']:
            raise ValueError
        if seq[0] == '#':
            return data_base.get_sequence_data_by_id(seq[1:])
        else:
            return seq[1:]

    def get_sequence(self, seq):
        data_base = DataBase()
        if seq[0] not in ['#', '@']:
            raise ValueError
        if seq[0] == '#':
            return data_base.get_sequence_data_by_name(data_base.get_sequence_data_by_id(seq[1:]))
        else:
            return data_base.get_sequence_data_by_name(seq[1:])

    def get_id(self, seq):
        data_base = DataBase()
        if seq[0] == '#':
            return seq[1:]
        if seq[0] == '@':
            return data_base.get_id(seq[1:])
        raise ValueError

    def validate_name(self, name, char):
        data_base = DataBase()
        origin_name = name
        id = 1
        while data_base.name_exist(name) is not None:
            name = origin_name + '_' + char + str(id)
            id += 1
        return name

    def print(self, id, name, sequence):
        print('[{}] {}: {}'.format(id, name, sequence))

    def get_new_name(self, old_name, new_name, str):
        if new_name == '@@':
            return  self.validate_name(old_name, str)
        elif new_name[0] == "@":
            return self.validate_name(new_name[1:], str)
        else:
            raise ValueError