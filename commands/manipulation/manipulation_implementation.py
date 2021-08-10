try:
    from .pair_command import PairCommand
    from .slice_command import SliceCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
ManipulationImplementation class
'''


class ManipulationImplementation:
    def __init__(self):
        self.commands = {
            "slice": SliceCommand,
            "pair": PairCommand,
        }

    def get_command(self, args):
        if len(args) < 1:
            raise ValueError
        return self.commands[args[0]](args[1:])
