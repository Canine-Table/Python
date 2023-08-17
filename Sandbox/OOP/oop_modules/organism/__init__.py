from abc import ABC,abstractmethod
from typing import Optional
class Organism(ABC):

    __type_error_message: str = '{} must be defined and must be of type {}.'

    @abstractmethod
    def __init__(self, *, age: int,name: Optional[str] = None,) -> None:
        self._age = age
        self._name = name


    @property
    @abstractmethod
    def age(self):
        return self._age

    @age.setter
    @abstractmethod
    def age(self,value: int) -> int:
        if isinstance(int(),type(value)):
            self._age = value
        else:
            raise TypeError(Organism.__type_error_message.format('age','int'))

    @property
    @abstractmethod
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    @abstractmethod
    def name(self,value: Optional[str]) -> None:
        if isinstance(None,value):
            del self._name
        elif isinstance(str(),type(value)):
            self._name = value
        else:
            raise TypeError(Organism.__type_error_message.format('name','str'))
