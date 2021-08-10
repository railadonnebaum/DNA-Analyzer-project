try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
'''
BatchShow Command.
command: batchshow <@batch_name>
'''


class BatchShowCommand:
    def __init__(self, args):
        self.__name = args[0][1:]

    def execute(self):
        data_base = DataBase()
        batch_commands = data_base.get_batch_commands(self.__name).get_commands()
        for command in batch_commands:
            print(command)
