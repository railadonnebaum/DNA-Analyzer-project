"""
Data Structure.
hold two dictionaries:
#1: {id: name}
#2: {name:sequence}
"""

class DataBase:
    __instance = None
    __sequence_data_id_name = {}
    __sequence_data_name_sequence = {}
    __batch_data = {}

    def __new__(cls, *args, **kwargs):
        if not DataBase.__instance:
            DataBase.__instance = object.__new__(cls)
        return DataBase.__instance

    def insert_sequence_data_by_id(self, id, name):
        self.__sequence_data_id_name[id] = name

    def insert_sequence_data_by_name(self, name, seq):
        self.__sequence_data_name_sequence[name] = seq

    def name_exist(self, name):
        return self.__sequence_data_name_sequence.get(name)

    def get_sequence_data_by_id(self, id):
        return self.__sequence_data_id_name.get(int(id))

    def get_sequence_data_by_name(self, name):
        return self.__sequence_data_name_sequence.get(name)

    def set_sequence_data_by_name(self, name, new_sequence):
        self.__sequence_data_name_sequence[name] = new_sequence

    def delete_from_dna_sequence_data(self, del_id, del_name):
        del self.__sequence_data_name_sequence[del_name]
        del self.__sequence_data_id_name[int(del_id)]

    def get_id(self, name):
        for key, value in self.__sequence_data_id_name.items():
            if name == value:
                return key
        return None

    def insert_batch(self, name, commandList):
        DataBase.__batch_data[name] = commandList

    def get_commands(self, name):
        return self.__batch_data.get(name)

    def get_batch_names(self):
        return self.__batch_data.keys()

    def get_batch_commands(self, name):
        return self.__batch_data[name]


