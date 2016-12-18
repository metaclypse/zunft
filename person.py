#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

GENDER_MALE = 0
GENDER_FEMALE = 1

PROF_BLACKSMITH = 0
PROF_ALCHEMIST = 1
PROF_PERFUMER = 2
PROF_PRIEST = 3

RELIGION_KATHOLISCH = 0
RELIGION_KATHARISCH = 1

MAX_STAT = 24
MAX_RANK = 5
MAX_STANDING = 5
MAX_WEALTH = 1000000
MAX_AP = 20

SKIN_PATHS = ["", "", ""]
CREST_PATHS = ["", "", ""]
FUNCTIONS = ["", "", ""]

GENDER = {
    GENDER_MALE: "Mann",
    GENDER_FEMALE: "Frau"
}

PROFESSIONS = {
    PROF_BLACKSMITH: "Schmied",
    PROF_ALCHEMIST: "Trankmischer",
    PROF_PERFUMER: "Duftmischer",
    PROF_PRIEST: "Prediger"
}

STADINGS = {
    0: "Herr",
    1: "Bürger",
    2: "Patrizier",
    3: "Edelmann",
    4: "Graf"
}


class Person:
    def __init__(self, pid, first_name, last_name, father, mother, gender, religion, skin, talents, fortune, profession,
                 crest=None, rank=0, standing=0, function=0, ap=0):
        self.id = pid
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
        self.mother = mother
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
        pass  # TODO

    @staticmethod
    def random_person(pid, auto_save=False):
        rnd_gender = random.randint(GENDER_MALE, GENDER_FEMALE)
        rnd_last_name = Person.get_random_last_name()
        rnd_first_name = Person.get_random_name(rnd_gender)

        rnd_father = None
        rnd_mother = None

        rnd_religion = random.randint(RELIGION_KATHOLISCH, RELIGION_KATHARISCH)

        rnd_skin = random.randint(0, len(SKIN_PATHS) - 1)
        rnd_crest = random.randint(0, len(CREST_PATHS) - 1)

        rnd_talents = Talents(random.randint(1, MAX_STAT),
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
        name_file = "./res/family_names.txt"

        with open(name_file) as f:
            lines = f.read().splitlines()
            f.close()

        rnd_id = random.randint(0, len(lines) - 1)

        return lines[rnd_id]

    def get_sympathy(self, pid):
        return self.sympathy[pid]

    def set_sympathy(self, pid, val):
        self.sympathy[pid] = val

    def to_string(self):
        txt = "ID: " + str(self.id) + \
              "\nName: " + self.first_name + " " + self.last_name + \
              "\nGender: " + str(self.gender) + \
              "\nAP: " + str(self.ap) +  \
              "\nProfession: " + PROFESSIONS[self.profession]

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
        self.night = n
        self.fighting = f
        self.trading = t
        self.craft = c
        self.rhetorics = r


class Wealth:
    def __init__(self, c1, c2, c3, c4):
        self.km = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

if __name__ == "__main__":
    print("__Test__")
    p1 = Person.random_person(1)
    print(p1.to_string())
