from abc import ABC,ABCMeta,abstractmethod
from typing import Optional,Any
from collections.abc import Sequence


class GetSetParent(ABC):

    __metaclass__: type[ABCMeta] = ABCMeta

    def __init__(self,value: Any) -> None:
        self.__val = value

    @property
    @abstractmethod
    def val(self) -> Any:
        return self.__val

    @val.setter
    def val(self,value: int) -> None:
        self.__val = value

    @property
    @abstractmethod
    def doc(self) -> str:
        return self.__doc__

    @doc.setter
    def doc(self,doc) -> None:
        self.__doc__ = doc


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
        if isinstance(list(),type(value)):
            self.__val = value
        else:
            self.__val = []

    @property
    def val(self) -> list:
        return self.__val

    @val.setter
    def val(self,value: list) -> None:
        if isinstance(list(),type(value)):
            self.__val = value
        else:
            self.__val = []

    @property
    def doc(self) -> str:
        return self.__doc__

    @doc.setter
    def doc(self,value: str) -> None:
        if isinstance(str(),type(value)):
            self.__doc__ = value
        else:
            self.__doc__ = 'Must be a string'
