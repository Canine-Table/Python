#!/usr/bin/python3
from typing import Any
from oop_modules.store import Item


class Phone(Item):

    def __init__(self, name: str, price: float, **kwargs: Any) -> None:
        # call to super function to have access to all attributes/methods
        super().__init__(name,price,**kwargs)
        self.broken_phone: bool = kwargs.get('broken_phone',False)

        # Actions to execute
        Phone.all.append(self)
