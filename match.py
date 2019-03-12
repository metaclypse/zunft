#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person, GENDER_MALE, MAX_SYMPATHY
# noinspection PyUnresolvedReferences
import city, building
from random import randint
from game_utils import probability

import datetime
import logging

import sys
reload(sys)

# noinspection PyUnresolvedReferences
sys.setdefaultencoding('utf8')

NONE = -1

START_DATE = datetime.datetime(1400, 4, 1)  # start: 1st of April, 1400 (we always start in spring)
ROUND_LENGTH_SECONDS = 10 #* 60  # 10 minutes per round (day)
TICK_TIME = 30  # 1 tick every thirty updates with 30 fps

SPOUSE_PROBABILITY = 25  # in %
RELATIVE_PROBABILITY = 33  # in %
RIVAL_COUNT = 4

SEASON_SPRING = 0
SEASON_SUMMER = 1
SEASON_AUTUMN = 2
SEASON_WINTER = 3


# A match is one party of a "game", but that name is taken already
class Match(object):
    def __init__(self, context):
        self.context = context

        self.city = None
        self.buildings = []
        self.persons = []  # list of person objects
        self.rivals = []  # list of indexes of "persons" list

        self.season = SEASON_SPRING
        self.date = START_DATE
        self.day_step = datetime.timedelta(1)

        self.player_event_times = []
        self.history_event_times = []

        self.update_counter = 0

        self.total_ticks = 0  # fixme: this might overflow...

        for i in range(0, 20):
            self.persons.append(Person.random_person(i))

        person_max = len(self.persons) - 1

        # initialize person sympathy lists
        # for now only randomly
        for p in self.persons:
            for i in range(0, len(self.persons)):
                sympathy_border = 10
                p.sympathy.append(randint(sympathy_border, MAX_SYMPATHY - sympathy_border))

        logging.debug("created sympahthy lists")

        # make some people relatives
        # todo: also randomly, only for the beginning! this makes no sense
        for p in self.persons:
            if probability(RELATIVE_PROBABILITY):  # chance that the person gets relatives
                p.father = randint(0, person_max)
                p.mother = randint(0, person_max)

        # make some people spouses
        for p in range(0, len(self.persons)):
            if probability(SPOUSE_PROBABILITY):  # chance that the person gets a spouse

                # throw dice for candidate
                candidate = p
                while candidate == p:
                    candidate = randint(0, person_max)

                # check if candidate related to p or same sex
                if candidate == self.persons[p].father or candidate == self.persons[p].mother:
                    logging.debug('cannot make {} and {} spouses: candidate is parent'.format(p, candidate))
                elif self.persons[candidate].mother == p or self.persons[candidate].father == p:
                    logging.debug('cannot make {} and {} spouses: candidate is child'.format(p, candidate))
                elif self.persons[p].gender == self.persons[candidate].gender:
                    # in the middle ages this was taboo
                    # also makes child generation easier
                    logging.debug('cannot make {} and {} spouses: same gender'.format(p, candidate))
                else:
                    logging.debug('making {} and {} spouses'.format(p, candidate))
                    # setting spouse value
                    self.persons[p].spouse = candidate
                    self.persons[candidate].spouse = p

                    # setting sympathy to 100%, because spouses love one another!
                    self.persons[p].sympathy[candidate] = MAX_SYMPATHY
                    self.persons[candidate].sympathy[p] = MAX_SYMPATHY

                    # change last name of woman to man's (this is the middle ages)
                    if self.persons[p].gender == GENDER_MALE:
                        self.persons[candidate].last_name = self.persons[p].last_name
                    else:
                        self.persons[p].last_name = self.persons[candidate].last_name

        # make some people into rivals for the player
        # these are the most important persons in the game
        # todo rival creation
        for i in range(RIVAL_COUNT):
            candiate = NONE
            while candidate == NONE or candidate in self.rivals:
                candidate = randint(0, person_max)

            self.rivals.append(candidate)

        # create city
        self.city = city.City(city.CITY_COLOGNE)  # todo: allow choice of city
        # finances
        # positions

        # create buildings
        # some random, others fixed (depending on city)

        logging.debug('match setup complete')

    def tick(self):
        self.total_ticks += 1
        logging.debug("tick() #" + str(self.total_ticks) + "")

        # let persons perform their strategies

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

        if self.total_ticks >= ROUND_LENGTH_SECONDS:
            self.next_day()

    def next_day(self):
        logging.debug('next_day()')
        self.date += self.day_step
        self.total_ticks = 0

        # generate player_event timing
        self.player_event_times = []
        for i in range(1, randint(2,4)):
            self.player_event_times.append(randint(0, ROUND_LENGTH_SECONDS))

        # generate history_event timing
        self.history_event_times = []
        for i in range(0, randint(0,2)):
            self.history_event_times.append(randint(0, ROUND_LENGTH_SECONDS))

    def update(self):
        if self.update_counter >= TICK_TIME:
            self.tick()
            self.update_counter = 0
        else:
            self.update_counter += 1
