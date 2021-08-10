try:
    from Batch.batch_observer import BatchObserver
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
'''
BatchLoad Command
command: batchload <filename> [:<batch_name>]
if file_name is not provided a default name is set to be: filename.
'''


class BatchLoadCommand:
    def __init__(self, args):
        self.__file = args[0] + '.dnabatch'
        if len(args) > 1:
            self.__name = args[2][1:]
        else:
            self.__name = args[0]

    def execute(self):
        data_base = DataBase()
        commands = []
        try:
            with open('resources/' + self.__file, 'r') as loadBatchFile:
                for line in loadBatchFile:
                    commands.append(line)
                batch_observer = BatchObserver([self.__name], commands)
                data_base.insert_batch(self.__name, batch_observer)
        except IOError:
            raise IOError
