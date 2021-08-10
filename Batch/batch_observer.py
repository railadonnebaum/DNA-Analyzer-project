try:
    from Batch.batch import Batch
    from commands.command_implementation import CommandImplementation
except ImportError:
    print("Need to fix the installation")
    raise
'''
Batch Observer
'''


class BatchObserver:
    def __init__(self, args, commands=None):
        if commands is None:
            commands = []
        self.__commands = commands
        self.__name = args[0]
        self.__command_implementation = CommandImplementation()

    def run(self):
        batch = Batch()
        batch.run(self)

    def notify(self):
        for command in self.__commands:
            commandList = command.split()
            command = self.__command_implementation.get_command(commandList)
            command.execute()

    def attach(self, command):
        self.__commands.append(command)

    def get_commands(self):
        return self.__commands

    def get_name(self):
        return self.__name
