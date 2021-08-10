try:
    from .data_base import DataBase
except ImportError:
    print("Need to fix the installation")
    raise
'''
Class Dna
'''


class Dna:
    __id = 1

    def __init__(self, dna_sequence, name):
        self.__name = name
        self.__id = Dna.__id
        self.__dna_sequence = dna_sequence
        self.__database = DataBase()

    @staticmethod
    def get_id():
        return Dna.__id

    def get_name(self):
        return self.__name

    def get_dna_sequence(self):
        return str(self.__dna_sequence)

    def execute(self):
        self.__database.insert_sequence_data_by_name(self.__name, self.__dna_sequence)
        self.__database.insert_sequence_data_by_id(self.__id, self.__name)
        Dna.__id += 1
