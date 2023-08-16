#!/usr/bin/python3
from abc import ABC,abstractmethod

class Vehicle(ABC):

    all = []

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
