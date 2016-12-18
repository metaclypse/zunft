#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person
from random import randint


# A match is one party of a "game", but that name is taken already
class Match:
    def __init__(self):
        self.persons = []

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


if __name__ == "__main__":
    print("__Test__")
    m = Match()

    print(str(m.persons[1].get_sympathy(2)))
