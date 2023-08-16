#!/usr/bin/python3
from collections.abc import Iterator,Callable,Collection,Iterable,Sequence
from typing import Union,Any,Optional,List,Dict


class TypeHinting:
    pass
    NUMBERS = Union[int,float]

    @staticmethod
    def custom_map(func: Callable[[Any],Any], sequence: Sequence[Any]) -> Iterator[str]:
        for el in sequence:
            yield str(func(el))


    @staticmethod
    def applying(func: Callable[[NUMBERS],NUMBERS], values: Iterable[Iterable[NUMBERS]]) -> Iterator[NUMBERS]:
        for value1, value2 in values:
            yield func(value1,value2)
