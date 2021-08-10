try:
    from .analysis_commands import AnalysisCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
Find Command.
command: find <seq> <sub_seq>
seq might be a seq id: #id, or a seq name: #name.
sub seq might be a string or an existing sequence.
'''


class FindCommand(AnalysisCommand):
    def __init__(self, args):
        seq, sub_seq = self.parse(args)
        self.__sequence = self.get_sequence(seq)
        self.__sub_sequence = self.get_sub_sequence(sub_seq)

    def execute(self):
        print(str(self.__sequence).find(str(self.__sub_sequence)))
