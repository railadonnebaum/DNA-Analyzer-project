try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
'''
BatchList Command.
command: batchlist 
'''


class BatchListCommand:
    def __init__(self, args):
        pass

    def execute(self):
        data_base = DataBase()
        batch_names = data_base.get_batch_names()
        print(list(batch_names))
