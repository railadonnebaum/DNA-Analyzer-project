try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
'''
BatchSave Command
command: batchsave <@batch_name> [<filename>]
if file_name is not provided a default name is set to be: batch_name.
'''


class BatchSaveCommand:
    def __init__(self, args):
        self.__name = args[0][1:]
        if len(args) > 1:
            self.__file = args[1] + '.dnabatch'
        else:
            self.__file = args[0][1:] + '.dnabatch'

    def execute(self):
        data_base = DataBase()
        batch_commands = data_base.get_batch_commands(self.__name).get_commands()
        try:
            with open('resources/' + self.__file, 'w') as saveBatchFile:
                for command in batch_commands:
                    saveBatchFile.write(command + '\n')
        except IOError:
            raise IOError
