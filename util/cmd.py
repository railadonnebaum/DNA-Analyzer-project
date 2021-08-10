try:
    from commands.command_implementation import CommandImplementation
    from Batch.load_batch_command import BatchLoadCommand
except ImportError:
    print("Need to fix the installation")
    raise
'''
cmd class
'''


class Cmd:
    def __init__(self):
        self.__command_implementation = CommandImplementation()

    def run(self, commandList):
        if commandList[0] == 'batchload':
            command = BatchLoadCommand(commandList[1:])
            command.execute()
        else:
            command = self.__command_implementation.get_command(commandList)
            command.execute()
