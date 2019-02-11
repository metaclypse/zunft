#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json

GENDER_MALE = 0
GENDER_FEMALE = 1

PROF_BLACKSMITH = 0
PROF_ALCHEMIST = 1
PROF_PERFUMER = 2
PROF_PRIEST = 3
PROF_GUARD = 4
PROF_THIEF = 5
PROF_MASON = 6
PROF_CARPENTER = 7
PROF_HOST = 8
PROF_ROBBER = 9
PROF_MERCHANT = 10

RELIGION_KATHOLISCH = 0
RELIGION_KATHARISCH = 1

MAX_STAT = 24  # 4x4 pts = 4 stars are maximum, 4 pts are worth one star, for every improvement the caracter gains 1 pt
MAX_RANK = 5
MAX_WEALTH = 1000000
MAX_AP = 20
MAX_STANDING = 4

DEFAULT_MONEY = 1000  # 1000 moneys as starting capital

SKIN_PATHS = ["", "", ""]
CREST_PATHS = ["", "", ""]
FUNCTIONS = ["", "", ""]

GENDER_STRINGS = {
    GENDER_MALE: "Mann",
    GENDER_FEMALE: "Frau"
}

PROFESSION_STRINGS = {
    PROF_BLACKSMITH: "Schmied",
    PROF_ALCHEMIST: "Trankmischer",
    PROF_PERFUMER: "Duftmischer",
    PROF_PRIEST: "Prediger"
}


STANDING_STRINGS = {
    0: "Herr",
    1: "Bürger",
    2: "Patrizier",
    3: "Edelmann",
    4: "Graf"
}


class Person(object):
    def __init__(self, pid, first_name, last_name, father, mother, gender, religion, skin, talents, fortune, profession,
                 crest=None, rank=0, standing=0, function=0, ap=0, spouse=-1):
        self.id = pid
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
        self.mother = mother
        self.spouse = spouse
        self.gender = gender
        self.religion = religion
        self.skin = skin
        self.crest = crest
        self.talents = talents
        self.standing = standing
        self.function = function
        self.profession = profession
        self.rank = rank
        self.ap = ap
        self.fortune = fortune
        self.sympathy = []

    @staticmethod
    def from_save(pid):
        pass  # TODO lol

    @staticmethod
    def random_person(pid, auto_save=False):
        rnd_gender = random.randint(GENDER_MALE, GENDER_FEMALE)
        rnd_last_name = Person.get_random_last_name()
        rnd_first_name = Person.get_random_name(rnd_gender)

        rnd_father = -1
        rnd_mother = -1

        rnd_religion = random.randint(RELIGION_KATHOLISCH, RELIGION_KATHARISCH)

        rnd_skin = random.randint(0, len(SKIN_PATHS) - 1)
        rnd_crest = random.randint(0, len(CREST_PATHS) - 1)

        rnd_talents = Talents(random.randint(1, MAX_STAT),  # todo: change max stats of others according to difficulty
                              random.randint(1, MAX_STAT),
                              random.randint(1, MAX_STAT),
                              random.randint(1, MAX_STAT),
                              random.randint(1, MAX_STAT))
        rnd_standing = random.randint(0, MAX_STANDING)
        rnd_function = 0
        rnd_profession = random.randint(0, len(FUNCTIONS))
        rnd_rank = random.randint(0, MAX_RANK)
        rnd_ap = random.randint(0, MAX_AP)
        rnd_fortune = Wealth(random.randint(0, MAX_WEALTH),
                             random.randint(0, MAX_WEALTH),
                             random.randint(0, MAX_WEALTH),
                             random.randint(0, MAX_WEALTH))

        return Person(pid,
                      rnd_first_name,
                      rnd_last_name,
                      rnd_father,
                      rnd_mother,
                      rnd_gender,
                      rnd_religion,
                      rnd_skin,
                      rnd_talents,
                      rnd_fortune,
                      rnd_profession,
                      rnd_crest,
                      rnd_rank,
                      rnd_standing,
                      rnd_function,
                      rnd_ap)

    @staticmethod
    def get_random_name(gender):
        if gender == GENDER_MALE:
            name_file = "./res/male_names.txt"
        elif gender == GENDER_FEMALE:
            name_file = "./res/female_names.txt"

        with open(name_file) as f:
            lines = f.read().splitlines()
            f.close()

        rnd_id = random.randint(0, len(lines) - 1)

        return lines[rnd_id]

    @staticmethod
    def get_random_last_name():
        name_file = './res/family_names.json'

        # with open(name_file) as f:
        #     lines = f.read().splitlines()
        #     f.close()
        #
        # rnd_id = random.randint(0, len(lines) - 1)
        #
        # return lines[rnd_id]

        with open(name_file) as f:
            name_data = json.load(f)

            name_list = name_data['last_names']
            rnd_id = random.randint(0, len(name_list) - 1)
            return name_list[rnd_id]

    def get_sympathy(self, pid):
        return self.sympathy[pid]

    def set_sympathy(self, pid, val):
        self.sympathy[pid] = val

    def to_string(self):
        txt = "ID: " + str(self.id) + \
              "\nName: " + self.first_name + " " + self.last_name + \
              "\nGender: " + str(self.gender) + \
              "\nAP: " + str(self.ap) +  \
              "\nProfession: " + PROFESSION_STRINGS[self.profession]

        return txt


class Relationships:
    def __init__(self):
        self.relationships = []
        self.relationships.append([])

    def get_liking(self, person1, person2):
        id1 = person1.id
        id2 = person2.id
        return self.relationships[id1][id2]

    def set_liking(self, person1, person2, val):
        id1 = person1.id
        id2 = person2.id
        self.relationships[id1][id2] = val


class Talents:
    def __init__(self, n, f, t, c, r):
        self.night = n  # Bei Nacht und Nebel
        self.fighting = f  # Kampf
        self.trading = t  # Verhandeln
        self.craft = c  # Handwerkskunst
        self.rhetoric = r  # Rhetorik


class Wealth:
    # for different currencies, default is km
    def __init__(self, c1=DEFAULT_MONEY, c2=0, c3=0, c4=0):
        self.km = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

if __name__ == "__main__":
    print("__Test__")
    p1 = Person.random_person(1)
    print(p1.to_string())
