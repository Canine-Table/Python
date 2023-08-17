from oop_modules.organism.species import Species
from typing import Optional,Any

class Coil(Species):

    def __init__(self,**kwargs: Any) -> None:
        super().__init__(**kwargs)

    @property
    def age(self) -> int:
        super().age()

    @age.setter
    def age(self,value: int) -> None:
        super().age(value)

    @property
    def name(self) -> Optional[str]:
        super().name()

    @name.setter
    def name(self,value: Optional[str]) -> None:
        super().name(value)

    @property
    def species(self) -> str:
        super().species()

    @species.setter
    def species(self,value: str) -> None:
        super().species(value)

    @property
    def common_name(self) -> str:
        super().common_name()

    @common_name.setter
    def common_name(self, value: str) -> None:
        super().common_name(value)
