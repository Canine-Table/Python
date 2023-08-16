from abc import ABC,ABCMeta,abstractmethod


class GetterSetter(ABC):

    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def val(self):
        return


class ABCClass(GetterSetter):

    string: str = str

    @property
    def val(self) -> str:
        return self.string

    @val.setter
    def val(self,value) -> None:
        self.string = value
