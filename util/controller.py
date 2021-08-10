try:
    from Batch.batch_observer import BatchObserver
    from util.cmd import Cmd
except ImportError:
    print("Need to fix the installation")
    raise
'''
Controller - runs the commands.

in order to begin a batch mode, the user most input: batch <batch_name>.
'''


class Controller:
    def __init__(self):
        self.__cmd = Cmd()

    def run(self, command):
        try:
            commandList = command.split()
            if commandList[0] == 'batch':
                batchObserver = BatchObserver(commandList[1:])
                batchObserver.run()
            else:
                self.__cmd.run(commandList)
        except Exception as e:
            print('Error', e)
