try:
    from .count_command import CountCommand
    from .find_all_command import FindAllCommand
    from .find_command import FindCommand
    from .len_command import LenCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
class AnalysisImplementation
'''


class AnalysisImplementation:
    def __init__(self):
        self.commands = {
            "find": FindCommand,
            "findall": FindAllCommand,
            "len": LenCommand,
            "count": CountCommand,
        }

    def get_command(self, args):
        if len(args) < 1:
            raise ValueError
        return self.commands[args[0]](args[1:])
