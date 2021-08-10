try:
    from .del_command import DelCommand
    from .save_command import SaveCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
ManagementImplementation class
'''


class ManagementImplementation:
    def __init__(self):
        self.commands = {
            "del": DelCommand,
            "save": SaveCommand,
        }

    def get_command(self, args):
        if len(args) < 1:
            raise ValueError
        return self.commands[args[0]](args[1:])
