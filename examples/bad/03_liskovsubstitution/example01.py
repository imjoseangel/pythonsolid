#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

DEFAULT_LION_LEG_COUNT = 4
DEFAULT_MOUSE_LEG_COUNT = 4
DEFAULT_SNAKE_LEG_COUNT = 0


class Animal:
    pass


class Lion(Animal):
    pass


class Mouse(Animal):
    pass


class Snake(Animal):
    pass


def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(DEFAULT_LION_LEG_COUNT)
        elif isinstance(animal, Mouse):
            print(DEFAULT_MOUSE_LEG_COUNT)
        elif isinstance(animal, Snake):
            print(DEFAULT_SNAKE_LEG_COUNT)


def main():

    animals = [
        Lion(),
        Mouse(),
        Snake()
    ]

    animal_leg_count(animals)


if __name__ == '__main__':
    main()
