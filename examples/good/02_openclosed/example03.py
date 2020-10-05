#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2


def main():

    customer, price = 'Jan', 100

    assert Discount(customer, price).get_discount() == 20.0
    assert VIPDiscount(customer, price).get_discount() == 40.0
    assert SuperVIPDiscount(customer, price).get_discount() == 80.0


if __name__ == '__main__':
    main()
