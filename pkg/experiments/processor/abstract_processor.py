import  abc
from materials.material import Material

class AbstractProcessor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def process(self, m: Material)->Material:
        pass
