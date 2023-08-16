#!/usr/bin/python3

class MaxSizeList(object):

    def __init__(self,max: int) -> None:
        self.max: int = max
        self.inner_list: list(str) = []

    def push(self, value: str) -> None:
        self.inner_list.append(str(value))
        if len(self.inner_list) > self.max:
            self.inner_list.pop(0)

    def get_list(self) -> object:
        print(self.inner_list)
        return self
