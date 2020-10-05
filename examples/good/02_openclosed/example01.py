#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'Roar!!!'


class Mouse(Animal):
    def make_sound(self):
        return 'Squeak!!!'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


def main():

    animals = [
        Lion('Lion'),
        Mouse('Mouse')
    ]

    animal_sound(animals)


if __name__ == '__main__':
    main()
