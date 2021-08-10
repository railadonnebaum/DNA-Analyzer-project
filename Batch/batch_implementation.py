try:
    from .batch_list_command import BatchListCommand
    from .batch_show_command import BatchShowCommand
    from .run_command import RunCommand
    from .saving_batch_command import BatchSaveCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
class Batch Implementation
'''


class BatchImplementation:
    def __init__(self):
        self.commands = {
            "run": RunCommand,
            "batchlist": BatchListCommand,
            "batchshow": BatchShowCommand,
            "batchsave": BatchSaveCommand
        }

    def get_command(self, args):
        if len(args) < 1:
            raise ValueError
        return self.commands[args[0]](args[1:])
