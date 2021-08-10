"""
Class DnaSequence
"""


class DnaSequence:
    def __init__(self, string):
        if type(string) is not str:
            raise TypeError
        if not validate_dna_sequence(string):
            raise ValueError
        self.__dna_sequence = string

    def insert(self, value, index):
        if index > len(self) or index < 0:
            raise IndexError
        if type(index) is not int or type(value) is not str:
            raise ValueError
        if not validate_dna_sequence(value):
            raise ValueError
        self.__dna_sequence = self.__dna_sequence[:index] + value + self.__dna_sequence[index:]

    def assignment(self, new_value):
        if type(new_value) is str:
            if not validate_dna_sequence(new_value):
                raise ValueError
            self.__dna_sequence = new_value
        elif type(new_value) is DnaSequence:
            self.__dna_sequence = new_value.get_dna_sequence()
        else:
            raise TypeError

    def __str__(self):
        return self.__dna_sequence

    def __eq__(self, other):
        if type(other) is str:
            return self.__dna_sequence == other
        elif type(other) is DnaSequence:
            return self.__dna_sequence == other.get_dna_sequence()
        else:
            raise TypeError

    def __ne__(self, other):
        return self.__dna_sequence != other.get_dna_sequence()

    def __getitem__(self, item):
        return self.__dna_sequence[item]

    def __setitem__(self, key, value):
        if key > len(self) or key < 0:
            raise IndexError
        if type(key) is not int or type(value) is not str:
            raise ValueError
        if not validate_dna_sequence(value):
            raise ValueError
        self.__dna_sequence = self.__dna_sequence[:key] + value + self.__dna_sequence[key + 1:]

    def __len__(self):
        return len(self.__dna_sequence)


def validate_dna_sequence(string):
    return all(char in 'ACGT' for char in string)
