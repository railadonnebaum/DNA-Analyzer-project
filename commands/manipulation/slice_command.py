try:
    from commands.manipulation.manipulation_commands import ManipulationCommands
    from dna.data_base import DataBase
    from dna.dna import Dna
except ImportError:
    print("Need to fix the installation")
    raise
'''
slice Command.
command: dup <seq> <from_index> <to_index> [: @<new_name> | @@]
seq might be a seq id: #id, or a seq name: #name.
if name is not provided the slice command changes the original seq, if @@ is provided,
a default name is set to be <original_name_s1>
'''


class SliceCommand(ManipulationCommands):
    def __init__(self, args):
        data_base = DataBase()
        dna_id, start_index, end_index, new_name = self.parse(args)
        self.__id = self.get_id(dna_id)
        self.__name = self.get_name(dna_id)
        self.__dna_sequence = self.get_sequence(dna_id)
        self.__dna_sequence = self.__dna_sequence[int(start_index):int(end_index)]
        self.__dna = None
        if new_name is not None:
            self.__name = self.get_new_name(self.__name, new_name, 's')
            self.__dna = Dna(self.__dna_sequence, self.__name)
        else:
            data_base.set_sequence_data_by_name(self.__name, self.__dna_sequence)

    def execute(self):
        if self.__dna is not None:
            self.print(Dna.get_id(), self.__name, self.__dna_sequence)
            self.__dna.execute()
        else:
            self.print(self.__id, self.__name, self.__dna_sequence)
