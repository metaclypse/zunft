#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person
from random import randint

import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# A match is one party of a "game", but that name is taken already
class Match:
    def __init__(self):
        self.persons = []
        self.start_date = datetime.datetime(1400, 1, 1)

        self.date = self.start_date
        self.day_step = datetime.timedelta(1)

        for i in range(0, 5):
            self.persons.append(Person.random_person(i))

        # initialize person sympathy lists
        for p in self.persons:
            for i in range(0, len(self.persons)):
                p.sympathy.append(randint(10, 90))

        # make some people relatives
        # TODO

        # make some people spouses
        # TODO

    def next_day(self):
        self.date += self.day_step

    def update(self):
        # update


if __name__ == "__main__":
    print("__Test__")
    m = Match()



