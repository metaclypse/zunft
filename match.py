#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person
from random import randint

import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf8')

START_DATE = datetime.datetime(1400, 1, 1)
MATCH_LENGTH_SECONDS = 10 * 60  # 10 minutes
TICK_TIME = 30 # 1 tick every thirty updates by 30 fps


# A match is one party of a "game", but that name is taken already
class Match:
    def __init__(self, context):
        self.context = context

        self.persons = []

        self.date = START_DATE
        self.day_step = datetime.timedelta(1)

        self.player_event_times = []
        self.history_event_times = []

        self.second_counter = 0

        for i in range(0, 5):
            self.persons.append(Person.random_person(i))

        # initialize person sympathy lists
        # for now only randomly
        for p in self.persons:
            for i in range(0, len(self.persons)):
                p.sympathy.append(randint(10, 90))

        # make some people relatives
        # TODO

        # make some people spouses
        # TODO

    def setup(self):
        pass

    def tick(self):
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
        pass

    def next_day(self):
        self.date += self.day_step

        # generate player_event timing
        self.player_event_times = []
        for i in range(1, randint(2,4)):
            self.player_event_times.append(randint(0, MATCH_LENGTH_SECONDS))

        # generate history_event timing
        self.history_event_times = []
        for i in range(0, randint(0,2)):
            self.history_event_times.append(randint(0, MATCH_LENGTH_SECONDS))

    def update(self):
        if self.second_counter >= TICK_TIME:
            self.tick()
            self.second_counter = 0
        else:
            self.second_counter += 1


if __name__ == "__main__":
    print("__Test__")
    m = Match()
    m.next_day()



