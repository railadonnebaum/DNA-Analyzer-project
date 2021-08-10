try:
    from .analysis_commands import AnalysisCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
Len Command.
command: len <seq> 
seq might be a seq id: #id, or a seq name: #name.
'''


class LenCommand(AnalysisCommand):
    def __init__(self, args):
        seq = self.parse(args)
        self.__sequence = self.get_sequence(seq)

    def execute(self):
        print(len(self.__sequence))
