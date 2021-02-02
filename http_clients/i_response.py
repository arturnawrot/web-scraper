from abc import ABCMeta, abstractmethod

class IResponse:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_contents(self): raise NotImplementedError