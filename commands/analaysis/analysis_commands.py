try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
'''
AnalysisCommand Interface
'''


class AnalysisCommand:
    def __init__(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

    def parse(self, args):
        if len(args) > 1:
            return args[0], args[1]
        return args[0]

    def get_sequence(self, seq):
        data_base = DataBase()
        if seq[0] not in ['#', '@']:
            raise ValueError
        if seq[0] == '#':
            return data_base.get_sequence_data_by_name(data_base.get_sequence_data_by_id(seq[1:]))
        else:
            return data_base.get_sequence_data_by_name(seq[1:])

    def get_sub_sequence(self, sub_seq):
        data_base = DataBase()
        if sub_seq[0] == '#':
            return data_base.get_sequence_data_by_name(data_base.get_sequence_data_by_id(sub_seq[1:]))
        elif sub_seq[0] == '@':
            return data_base.get_sequence_data_by_name(sub_seq[1:])
        else:
            return sub_seq
