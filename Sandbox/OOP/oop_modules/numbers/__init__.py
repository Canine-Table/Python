#!/usr/bin/python3
from decimal import Decimal
from typing import Union,Any,Dict,List
from collections.abc import Sequence
NUMBERS = Union[float,int,Decimal]

class Numbers:
    __number: NUMBERS = 0

    def __init__(self,*args: Sequence(Any),**kwargs: Dict(str,NUMBERS)) -> None:
        self.__number: NUMBERS = kwargs.get('number',0)

    @property
    def number(self):
        return self.__number

    @number.deleter
    def number(self) -> None:
        self.__number = 0
