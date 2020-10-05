#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4


def main():

    customer1, price1 = 'fav', 100
    assert Discount(customer1, price1).get_discount() == 20.0

    customer2, price2 = 'vip', 100
    assert Discount(customer2, price2).get_discount() == 40.0


if __name__ == '__main__':
    main()
