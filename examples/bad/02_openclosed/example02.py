#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'Lion':
            print('Roar!!!')
        elif animal.name == 'Mouse':
            print('Squeak!!!')
        elif animal.name == 'Snake':
            print('Sssss!!!')


def main():

    animals = [
        Animal('Lion'),
        Animal('Mouse'),
        Animal('Snake')
    ]

    animal_sound(animals)


if __name__ == '__main__':
    main()
