try:
    from dna.data_base import DataBase
    from commands.managment.management_commands import ManagementCommands
except ImportError:
    print("Need to fix the installation")
    raise
'''
Delete Command.
command: del <seq>.
seq might be a seq id: #id, or a seq name: #name.
'''


class DelCommand(ManagementCommands):
    def __init__(self, args):
        self.__id = self.get_id(args[0])
        self.__name = self.get_name(args[0])
        self.__sequence = self.get_sequence(args[0])

    def execute(self):
        stdin = input(f"Do you really want to delete {self.__name}: {self.__sequence}?\n"
                      f"Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.\n"
                      f"confirm >>> ")
        while stdin not in ['y', 'Y', 'n', 'N']:
            print("You have typed an invalid response. "
                  "Please either confirm by 'y'/'Y', or"
                  " cancel by 'n'/'N'.")
            stdin = input("confirm >>> ")
        if stdin in ['Y', 'y']:
            delete_dna(self.__id, self.__name)
            print(f"Deleted: [{self.__id}] {self.__name}: {self.__sequence}")
        else:
            print('Canceled delete command.')


def delete_dna(id, name):
    data_base = DataBase()
    data_base.delete_from_dna_sequence_data(id, name)
