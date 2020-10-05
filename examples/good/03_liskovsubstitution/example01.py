#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

DEFAULT_LION_LEG_COUNT = 4
DEFAULT_MOUSE_LEG_COUNT = 4
DEFAULT_SNAKE_LEG_COUNT = 0


class Animal:
    def get_legs_count(self):
        pass


class Lion(Animal):
    def get_legs_count(self):
        return DEFAULT_LION_LEG_COUNT


class Mouse(Animal):
    def get_legs_count(self):
        return DEFAULT_MOUSE_LEG_COUNT


class Snake(Animal):
    def get_legs_count(self):
        return DEFAULT_SNAKE_LEG_COUNT


def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.get_legs_count())


def main():

    animals = [
        Lion(),
        Mouse(),
        Snake()
    ]

    animal_leg_count(animals)


if __name__ == '__main__':
    main()
