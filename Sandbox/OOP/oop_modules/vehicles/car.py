from oop_modules.vehicles import Vehicle
from typing import Optional,List
from datetime import datetime
class Car(Vehicle):


    __doc__: str = """_summary_
    this is a child class of the Vehicle class.
    this class is called Car and is the parent class
    of all 4 wheel road vehicles
    """

    all: List[object] = []
    __wheel_count: int = 4


    def __init__(self: object, owner: str, brand: str, model: str, *args, **kwargs) -> None:

        Car.all.append(self)
        self.__owner: str = owner
        self.__model: str = model
        self.__brand: str = brand
        self.__purchase_date: datetime.datetime = datetime.now()
        self.__color: Optional[str] = kwargs.get('color',None)
        self.__price: Optional[float] = kwargs.get('price',None)
        self.__year: Optional[int] = kwargs.get('year',None)
        self.__car_type: Optional[str] = kwargs.get('type',None)
        self.__door_count: Optional[int] = kwargs.get('door_count',None)
        self.__is_electric: bool = kwargs.get('is_electric',False)


    @property
    def purchase_date(self: object) -> str:
        return self.__purchase_date


    @property
    def price(self: object) -> Optional[float]:
        return self.__price

    @price.setter
    def price(self: object, value: float) -> None:
        self.__price: float = value


    @property
    def color(self: object) -> Optional[str]:
        return self.__color

    @color.setter
    def color(self: object, value: str) -> None:
        self.__color: str = value


    @property
    def car_type(self: object) -> Optional[str]:
        return self.__car_type

    @car_type.setter
    def car_type(self: object, value: str) -> None:
        self.__car_type: str = value


    @property
    def wheel_count(self: object) -> int:
        return self.__wheel_count


    @property
    def is_electric(self: object) -> bool:
        return self.__is_electric


    @property
    def year(self: object) -> Optional[int]:
        return self.__year


    @property
    def door_count(self: object) -> Optional[int]:
        return self.__door_count

    @door_count.setter
    def door_count(self: object, value: int) -> None:
        self.__door_count: int = value


    @property
    def owner(self: object) -> str:
        return self.__owner

    @owner.setter
    def owner(self: object, value: str) -> None:
        self.__owner: str = value


    @property
    def model(self: object) -> str:
        return self.__model


    @property
    def brand(self: object) -> str:
        return self.__brand


    def start(self: object) -> str:
        print(f'{self.owner} has started their {self.brand} {self.model}.')
        return self


    def stop(self: object) -> str:
        print(f'{self.owner} has stopped their {self.__brand} {self.model}.')
        return self


    def drive(self: object) -> str:
        print(f'{self.owner} has started to drive their {self.__brand} {self.model}.')
        return self


    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(owner="{self.owner}",brand="{self.brand}",model="{self.model}")'


    def __str__(self) -> str:
        return f'This {self.__class__.__name__} is a {self.brand} {self.model} which is owned by {self.owner} and purchased on {self.purchase_date}.'
