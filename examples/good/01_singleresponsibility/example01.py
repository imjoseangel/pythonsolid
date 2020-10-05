#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'My name is: {self.name}'


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        return f'Saving {animal.name} to DB'


def main():

    animal = Animal('Lion')
    db = AnimalDB()
    save = db.save(animal)
    print(save)


if __name__ == '__main__':
    main()
