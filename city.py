#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

CITY_COLOGNE = 0
CITY_AUGSBURG = 1
CITY_BERLIN = 2
CITY_DRESDEN = 3
CITY_HANNOVER = 4

CITY_SPECS = {
    CITY_COLOGNE: {
        'name': 'Köln',
        'specialty': 'Kurze Wege zum Kräutersuchen',
        'properties': 'Sehr viele',
        'difficulty': 'very easy',
        'player_count': 4
    },
    CITY_AUGSBURG: 'Augsburg',
    CITY_BERLIN: 'Berlin',
    CITY_DRESDEN: 'Dresden',
    CITY_HANNOVER: 'Hannover'
}


class LawSet(object):
    def __init__(self):
        self.bribing = True
        self.tax = 0.3

    @staticmethod
    def random_law_set():
        l = LawSet()

        l.bribing = bool(random.getrandbits(1))  # gives random bool
        l.tax = random.uniform(0, 1)  # gives a random number between 0 and 1

        return l


class City(object):
    def __init__(self, city_id):
        self.city_id = city_id
        self.laws = LawSet.random_law_set()
        self.money = 10000
        self.positions = []
