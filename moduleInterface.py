from abc import *

class moduleInterface(metaclass=ABCMeta):

    @abstractmethod
    def getAliases(self):
        pass

    @abstractmethod
    def getHelp(self):
        pass