#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person
from random import randint

import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf8')

start_date = datetime.datetime(1400, 1, 1)
match_length_seconds = 10 * 60


# A match is one party of a "game", but that name is taken already
class Match:
    def __init__(self):
        self.persons = []

        self.date = start_date
        self.day_step = datetime.timedelta(1)

        self.player_event_times = []
        self.history_event_times = []

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

    def tick(self):
        pass

    def next_day(self):
        self.date += self.day_step

        # generate player_event timing
        self.player_event_times = []
        for i in range(1, randint(2,4)):
            self.player_event_times.append(randint(0, match_length_seconds))

        # generate history_event timing
        self.history_event_times = []
        for i in range(0, randint(0,2)):
            self.history_event_times.append(randint(0, match_length_seconds))

    def update(self):
        pass

        # update buildings
        # calculate player_event probability
        # call player_event

        # calculate businesses
        # calculate production

        # calculate transaction probabilities
        # call transactions between npcs

        # calculate history_event probability
        # call history_event

        # update persons
        # * their relationships
        # * their assets


if __name__ == "__main__":
    print("__Test__")
    m = Match()
    m.next_day()



