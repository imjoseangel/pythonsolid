#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEFAULT_LION_LEG_COUNT = 4
DEFAULT_MOUSE_LEG_COUNT = 4


class Lion:

    def get_legs_count(self):
        print(DEFAULT_LION_LEG_COUNT)


class Mouse:

    def get_legs_count(self):
        print(DEFAULT_MOUSE_LEG_COUNT)


class Manager:

    def __init__(self):
        self.animal = None

    def set_animal(self, animal):
        assert isinstance(
            animal, Lion), "`animal` must be of type {}".format(Lion)

        self.animal = animal

    def get_legs_count(self):
        if self.animal is not None:
            self.animal.get_legs_count()


def main():

    lion = Lion()
    manager = Manager()
    manager.set_animal(lion)
    manager.get_legs_count()

    # The following will not work...
    mouse = Mouse()
    try:
        manager.set_animal(mouse)
    except AssertionError:
        print("Manager fails to support mouse...")


if __name__ == '__main__':
    main()
