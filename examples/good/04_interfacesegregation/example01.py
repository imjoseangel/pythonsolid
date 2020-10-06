#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

DEFAULT_LION_LEG_COUNT = 4
DEFAULT_MOUSE_LEG_COUNT = 4
DEFAULT_SNAKE_LEG_COUNT = 0


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def get_legs_count(self):
        pass


class Manager():

    def __init__(self):
        self.animal = None

    def set_animal(self, animal):
        assert isinstance(
            animal, Animal), "`animal` must be of type {}".format(Animal)

        self.animal = animal

    def get_legs_count(self):
        self.animal.get_legs_count()


class Lion(Animal):

    def get_legs_count(self):
        print(DEFAULT_LION_LEG_COUNT)


class Mouse(Animal):

    def get_legs_count(self):
        print(DEFAULT_MOUSE_LEG_COUNT)


class Snake(Animal):

    def get_legs_count(self):
        print(DEFAULT_SNAKE_LEG_COUNT)


def main():

    manager = Manager()
    manager.set_animal(Lion())
    manager.get_legs_count()

    manager.set_animal(Mouse())
    manager.get_legs_count()

    manager.set_animal(Snake())
    manager.get_legs_count()


if __name__ == '__main__':
    main()
