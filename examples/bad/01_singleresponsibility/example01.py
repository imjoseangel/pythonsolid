#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'

    def save(self, animal):
        return f'Saving {animal.name} to DB'


def main():
    animal = Animal('Lion')
    print(animal.save(animal))


if __name__ == '__main__':
    main()
