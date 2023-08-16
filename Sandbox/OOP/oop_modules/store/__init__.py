#!/usr/bin/python3
from typing import Union,Any
import csv


class Item:

    # The Pay rate after 20% discount
    pay_rate: float = 0.8
    all = []

    def __init__(self, name: str, price: float, **kwargs: Any) -> None:

        # run validations to received arguments
        assert price >= 0, f"Price '{price}' is not greater than or equal to zero!"
        assert kwargs.get('quantity',1) >= 0, f"Quantity '{kwargs['quantity']}' is not greater than or equal to zero!"

        # Assign to self object
        self.__name: str = name
        self.__price: float = price
        self.__quantity: int = kwargs.get('quantity',1)

        # Actions to execute
        Item.all.append(self)


    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self,value: str) -> None:
        self.__name = value


    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self,value: Union[int,float]) -> None:
        self.__price = value


    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self,value: int) -> None:
        self.__quantity = value

    @quantity.deleter
    def quantity(self) -> None:
        self.__quantity = 0


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num: Union[float,int]) -> bool:
        # We will count out the floats that are point 0
        # For example: 5.0, 7.0, 93.0
        if isinstance(num,float):
            return bool(num.is_integer)
        elif isinstance(num,int):
            return True
        return False

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self,**kwargs: float):
        self.price = self.price * kwargs.get('pay_rate',Item.pay_rate)
        return self.calculate_total_price()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = '{self.name}', price = {self.price}, quantity = {self.quantity})"
