try:
    from .dup_command import DupCommand
    from .load_command import LoadCommand
    from .new_command import NewCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
Creation Implementation class
'''


class CreationImplementation:
    def __init__(self):
        self.commands = {
            "new": NewCommand,
            "load": LoadCommand,
            "dup": DupCommand,
        }

    def get_command(self, args):
        if len(args) < 1:
            raise ValueError
        return self.commands[args[0]](args[1:])
