try:
    from dna.data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
'''
class Batch.
'''


class Batch:
    def __init__(self):
        pass

    def run(self, batchObserver):
        data_base = DataBase()
        batch_input = input("> batch >>> ")
        while batch_input != 'end':
            batchObserver.attach(batch_input)
            batch_input = input("> batch >>> ")
        data_base.insert_batch(batchObserver.get_name(), batchObserver)
