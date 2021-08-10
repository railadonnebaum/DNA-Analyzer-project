try:
    from abc import abstractmethod
except ImportError:
    print("Need to fix the installation")
    raise
'''
CLI - notifies the controller on income of input.
implement using the singleton and observer design pattern.
'''


class CLI:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not CLI.__instance:
            CLI.__instance = object.__new__(cls)
        return CLI.__instance

    def __init__(self, observer):
        self.__observers = [observer]

    def run(self):
        while True:
            command = input('cmd >>> ')
            if command == 'exit':
                break
            self.notify(command)

    @abstractmethod
    def attach(self, observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    @abstractmethod
    def detach(self, observer):
        try:
            self.__observers.pop(observer)
        except IndexError:
            pass

    @abstractmethod
    def notify(self, command):
        for observer in self.__observers:
            observer.run(command)



