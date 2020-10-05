#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self) -> str:
        return f'My name is: {self.name}'

    def get(self, id):
        return self.db.get_animal(id)

    def save(self):
        dbsave = self.db.save(animal=self)
        return dbsave


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        return f'Saving {animal.name} to DB'


animal = Animal('Lion')
animal.save()


def main():

    animal = Animal('Lion')
    save = animal.save()
    print(save)


if __name__ == '__main__':
    main()
