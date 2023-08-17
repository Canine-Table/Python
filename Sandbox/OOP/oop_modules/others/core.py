from collections.abc import Iterable
from typing import Union,Any
from typing_extensions import SupportsIndex


class Core:

    NUMBERS = Union[int,float]

    def __new__(cls,x: NUMBERS = 0, y: NUMBERS = 0) -> object:
        cls.x: cls.NUMBERS = x
        cls.y: cls.NUMBERS = y
        return cls

    def __new__(cls,x: bool = False, y: bool = False) -> object:
        cls.x: bool = x
        cls.y: bool = y
        return cls

    @staticmethod
    def print_result(function):
        def wrapper():
            print(function())
        return wrapper

    @print_result
    def addition() -> NUMBERS: return Core.x.__add__(Core.y)

    @print_result
    def subtraction() -> NUMBERS: return Core.x.__sub__(Core.y)

    @print_result
    def floor() -> NUMBERS: return Core.x.__floor__()

    @print_result
    def absolute() -> NUMBERS: return Core.x.__abs__()

    @print_result
    def ceiling() -> NUMBERS: return Core.x.__ceil__()

    @print_result
    def modulus() -> NUMBERS: return Core.x.__mod__(Core.y)

    @print_result
    def multiplication() -> NUMBERS: return Core.x.__mul__(Core.y)

    @print_result
    def division() -> NUMBERS: return Core.x.__truediv__(Core.y)

    @print_result
    def power() -> NUMBERS: return Core.x.__pow__(Core.y)

    @print_result
    def round() -> NUMBERS: return Core.x.__round__()

    @print_result
    def merge():
        return [x + y for x,y in zip(Core.x,Core.y)]

    @print_result
    def xor() -> bool: return Core.x.__xor__(Core.y)


    @print_result
    def lt() -> bool: return Core.x.__lt__(Core.y)

    @print_result
    def le() -> bool: return Core.x.__le__(Core.y)

    @print_result
    def gt() -> bool: return Core.x.__gt__(Core.y)

    @print_result
    def ge() -> bool: return Core.x.__ge__(Core.y)

    @print_result
    def eq() -> bool: return Core.x.__eq__(Core.y)

    @print_result
    def ne() -> bool: return Core.x.__ne__(Core.y)

    @print_result
    def ls() -> bool: return Core.x.__lshift__(Core.y)

    @print_result
    def rs() -> bool: return Core.x.__rshift__(Core.y)


class DunderCore:

    def __init__(self, this_list: list) -> None:
        self.my_list = this_list

    @staticmethod
    def print_result(function):
        def wrapper(*args):
            print(function(*args))
        return wrapper

    @print_result
    def __add__(self,other):
        return [x + y for x,y in zip(self.my_list,other.my_list)]

    @print_result
    def __sub__(self,other):
        return [x - y for x,y in zip(self.my_list,other.my_list)]

    @print_result
    def __mul__(self,other):
        return [x * y for x,y in zip(self.my_list,other.my_list)]

    @print_result
    def __pow__(self,other):
        return [x ** y for x,y in zip(self.my_list,other.my_list)]

    @print_result
    def __truediv__(self,other):
        return [x / y for x,y in zip(self.my_list,other.my_list)]

class DunderDictCore(dict):

    def __setitem__(self,k,v):
        dict.__setitem__(self,k,v)

class DunderListCore(list):

    def __getitem__(self,index: int) -> None:
        print(f'getting the item index {index}!')
        if index.__eq__(0): raise IndexError
        if index.__gt__(0): index = index - 1
        list.__getitem__(self,index)

    def __setitem__(self,index: int, value: Any) -> None:
        print(f'setting the index {index} to {value}!')
        if index.__eq__(0): raise IndexError
        if index.__gt__(0): index = index - 1
        list.__setitem__(self,index,value)

    def __delitem__(self, index: Union[SupportsIndex,slice]) -> None:
        print(f'deleting the index number {index}!')
        list.__delitem__(self,index)
