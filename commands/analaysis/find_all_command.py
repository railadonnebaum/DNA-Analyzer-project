try:
    import re

    from .analysis_commands import AnalysisCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
Find All Command.
command: findall <seq> <sub_seq>
seq might be a seq id: #id, or a seq name: #name.
sub seq might be a string or an existing sequence.
'''


class FindAllCommand(AnalysisCommand):
    def __init__(self, args):
        seq, sub_seq = self.parse(args)
        self.__sequence = self.get_sequence(seq)
        self.__sub_sequence = self.get_sub_sequence(sub_seq)

    def execute(self):
        res = [m.start() for m in re.finditer('(?={})'.format(str(self.__sub_sequence)), str(self.__sequence))]
        if res:
            for index in res:
                print(index, end=" ")
            print('')
        else:
            print('-1')
