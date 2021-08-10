try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
'''
BatchRun Command.
command: run <@batch_name>
'''


class RunCommand:

    def __init__(self, args):
        data_base = DataBase()
        name = args[0][1:]
        self.__commands = data_base.get_commands(name)

    def execute(self):
        self.__commands.notify()
