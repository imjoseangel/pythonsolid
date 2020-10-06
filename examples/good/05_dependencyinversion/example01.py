#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from abc import ABCMeta, abstractmethod
from six import with_metaclass

DEFAULT_LION_LEG_COUNT = 4
DEFAULT_MOUSE_LEG_COUNT = 4
DEFAULT_SNAKE_LEG_COUNT = 0


class Animal(with_metaclass(ABCMeta)):

    @abstractmethod
    def get_legs_count(self):
        pass


class Lion(Animal):

    def get_legs_count(self):
        print(DEFAULT_LION_LEG_COUNT)


class Mouse(Animal):

    def get_legs_count(self):
        print(DEFAULT_MOUSE_LEG_COUNT)


class Snake(Animal):

    def get_legs_count(self):
        print(DEFAULT_SNAKE_LEG_COUNT)


class Manager:

    def __init__(self):
        self.animal = None

    def set_animal(self, animal):
        assert isinstance(
            animal, Animal), "`animal` must be of type {}".format(Animal)

        self.animal = animal

    def get_legs_count(self):
        if self.animal is not None:
            self.animal.get_legs_count()


def main():

    lion = Lion()
    manager = Manager()
    manager.set_animal(lion)
    manager.get_legs_count()

    # The following will work!
    mouse = Mouse()
    try:
        manager.set_animal(mouse)
        manager.get_legs_count()
    except AssertionError:
        print("Manager fails to support mouse...")

    snake = Snake()
    manager.set_animal(snake)
    manager.get_legs_count()


if __name__ == '__main__':
    main()
