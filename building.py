#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAX_BUILDING_LEVEL = 3

BUILDING_UNKNOWN = -1
BUILDING_FORGE = 0
BUILDING_LABORATORY = 1
BUILDING_PARFUMERY = 2
BUILDING_CHURCH = 3
BUILDING_WATCH = 4
BUILDING_HIDEOUT = 5
BUILDING_MASON_WORKSHOP = 6
BUILDING_CARPENTER_WORKSHOP = 7
BUILDING_INN = 8
BUILDING_CASTLE = 9
BUILDING_TRADE_POST = 10
BUILDING_EXCHANGE_OFFICE = 11
BUILDING_CITY_HALL = 12


class Building(object):
    def __init__(self):
        self.health = 100
        self.name = None
        self.owner = None
        self.type = BUILDING_UNKNOWN
        self.extensions = []

    def extend(self):
        pass

    def upgrade(self):
        pass