from abc import ABC,ABCMeta,abstractmethod
from typing import Optional,Any
from collections.abc import Sequence


class GetSetParent(ABC):


    @abstractmethod
    def __init__(self,value: Any) -> None:
        self.val = value


    @abstractmethod
    def get_val(self) -> Any:
        return self.__val

    @abstractmethod
    def set_val(self,value: int) -> None:
        if isinstance(list(),type(value)):
            self.__val = value
        else:
            self.__val = []

    @abstractmethod
    def get_docs(self) -> str:
        return self.__doc__

    @abstractmethod
    def set_docs(self,value) -> None:
        self.__doc__ = value


    doc = property(fget=get_docs,fset=set_docs,doc="""
        This is some documents for property __doc__
        Keyword arguments:
        argument -- description
        Return: return_description
    """)

    val = property(fget=get_val,fset=set_val,doc="""
    Keyword arguments:
    argument -- description
    Return: return_description
    """)

class GetSetInt(GetSetParent):

    def __init__(self,value: int) -> None:
        if isinstance(int(),type(value)):
            self.__val = value
        else:
            self.__val = 0

    @property
    def val(self) -> Optional[int]:
        return self.__val

    @val.setter
    def val(self,value: int) -> None:
        if isinstance(int(),type(value)):
            self.__val = value
        self.__val = 0

    @property
    def doc(self) -> Optional[str]:
        return self.__doc__

    @doc.setter
    def doc(self,value: str) -> None:
        if isinstance(str,value):
            self.__doc__ = value
        self.__doc__ = 'Must be a string'
class GetSetList(GetSetParent):

    def __init__(self,value: Sequence) -> None:
        super().__init__(value)

    def get_val(self) -> list:
        return super().get_val()

    def set_val(self,value: list) -> None:
        super().set_val(value)

    def get_docs(self) -> str:
        return super().get_docs()

    def set_docs(self,value: str) -> None:
        super().set_docs(value)

    doc = property(fget=get_docs,fset=set_docs,doc="""
        This is some documents for property __doc__
        Keyword arguments:
        argument -- description
        Return: return_description
    """)

    val = property(fget=get_val,fset=set_val,doc="""
    Keyword arguments:
    argument -- description
    Return: return_description
    """)
