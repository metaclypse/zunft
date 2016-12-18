#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import person


S_INIT = 0

class Game:
    def __init__(self):
        self.state = S_INIT

    def run(self):
        print("starting")

        print("stopping")

if __name__ == "__main__":
    g = Game()
    g.run()
