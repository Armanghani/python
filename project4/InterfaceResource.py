from abc import ABC, abstractmethod

class Resource(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def modify(self, data):
        pass