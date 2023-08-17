from oop_modules.organism import Organism
from abc import abstractmethod
from typing import Optional,Any

class Species(Organism):


    @abstractmethod
    def __init__(self, *, species: str, common_name: str, **kwargs: Any) -> None:
        super().__init__(**kwargs)

        assert isinstance(str(),type(species)), Organism.__type_error_message.format('species','str')
        assert isinstance(str(),type(common_name)), Organism.__type_error_message.format('common_name','str')

        self._species = species
        self._common_name = common_name


    @property
    def age(self):
        super().age()

    @age.setter
    def age(self,value: int) -> int:
        super().age(value)

    @property
    def name(self) -> Optional[str]:
        super().name()

    @name.setter
    def name(self,value: Optional[str]) -> None:
        super().name(value)

    @property
    @abstractmethod
    def species(self) -> str:
        return self._species

    @species.setter
    @abstractmethod
    def species(self,value: str) -> str:
        if isinstance(str(),type(value)):
            self._species = value
        else:
            raise TypeError(super().__type_error_message.format('species','str'))

    @property
    @abstractmethod
    def common_name(self) -> str:
        return self._common_name

    @common_name.setter
    @abstractmethod
    def common_name(self, value: str):
        if isinstance(str(),type(value)):
            self._common_name = value
        else:
            raise TypeError(super().__type_error_message.format('common_name','str'))
