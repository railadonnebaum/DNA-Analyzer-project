try:
    from commands.analaysis.analaysis_implementation import AnalysisImplementation
    from Batch.batch_implementation import BatchImplementation
    from commands.creation.creation_implementation import CreationImplementation
    from commands.managment.managment_implementation import ManagementImplementation
    from commands.manipulation.manipulation_implementation import ManipulationImplementation
except ImportError:
    print("Need to fix the installation")
    raise
'''
factor - design pattern.
'''


class CommandImplementation:
    def __init__(self):
        self.commands = {
            "new": CreationImplementation,
            "load": CreationImplementation,
            "dup": CreationImplementation,
            "slice": ManipulationImplementation,
            "pair": ManipulationImplementation,
            "del": ManagementImplementation,
            "save": ManagementImplementation,
            "find": AnalysisImplementation,
            "findall": AnalysisImplementation,
            "len": AnalysisImplementation,
            "count": AnalysisImplementation,
            "run": BatchImplementation,
            "batchlist": BatchImplementation,
            "batchshow": BatchImplementation,
            "batchsave": BatchImplementation,
        }

    def get_command(self, args):
        try:
            if len(args) < 1:
                raise ValueError
            return self.commands[args[0]]().get_command(args)
        except Exception as e:
            print('Error', e)