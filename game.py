#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pygame
from pygame.locals import *
import sys

import menu
import match
import logging

# reload(sys)
# sys.setdefaultencoding('utf8')

S_NONE = -1
S_INIT = 0
S_MENU = 1
S_SETUP = 2
S_MATCH = 3
S_TRANSITION = 4
S_MAIN_MENU = 5
S_QUIT = 6

TARGET_FPS = 30


class Game:
    def __init__(self):
        self.state = S_INIT

        self.running = False
        self.title = "Die Zunft"

        self.all_sprites = pygame.sprite.Group()

        self.window = None
        self.fps_clock = None
        self.mouse_x, self.mouse_y = 0, 0
        self.click_down = False
        self.cursor = pygame.image.load("res/img/cursor.png")

        self.next_state = S_NONE

        self.main_menu = None
        self.match = None

    def schedule_state_change(self, state):
        self.next_state = state

    def start_game_setup(self):
        self.schedule_state_change(S_SETUP)

    def change_state(self):
        logging.debug("Changing to scheduled state " + str(self.next_state))
        self.state = self.next_state
        self.next_state = S_NONE

    def clear_sprites(self):
        self.all_sprites = pygame.sprite.Group()

    def setup_match(self):
        logging.debug("Setting up new match...")
        self.clear_sprites()

        self.match = match.Match(self)

        self.schedule_state_change(S_MATCH)

    def handle_events(self):
        handled_events = 0

        for event in pygame.event.get():
            # print("handling event #" + str(handled_events) + "(" + str(event) + ")")

            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEMOTION:
                self.mouse_x, self.mouse_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mouse_x, self.mouse_y = event.pos
                for s in self.all_sprites:
                    if s.rect.collidepoint((self.mouse_x, self.mouse_y)) and isinstance(s, menu.Button):
                        s.call_function()

            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_x, self.mouse_y = event.pos
                self.click_down = True
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    logging.debug("A was pressed")
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

            handled_events += 1

    def update(self):
        self.handle_events()

        self.all_sprites.update()
        s = self.state
        if s == S_INIT:
            pass
        if s == S_MAIN_MENU:
            if self.main_menu is None:
                self.main_menu = menu.MainMenu(self, (200, 100))

        elif s == S_MATCH:
            if self.match is None:
                self.setup_match()
            else:
                self.match.update()

        elif s == S_SETUP:
            self.setup_match()

        elif s == S_QUIT:
            self.running = False

        if self.next_state != S_NONE:
            self.change_state()

    def render(self):
        # clear screen
        self.window.fill(pygame.Color(255, 255, 255))

        # render sprites
        # self.all_sprites.clear(self.window)
        self.all_sprites.draw(self.window)

        pygame.display.flip()

        # render cursor
        self.window.blit(self.cursor, (self.mouse_x, self.mouse_y))

    def run(self):
        logging.debug("starting the program")

        pygame.init()
        pygame.mouse.set_visible(False)
        self.fps_clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((1024, 600))
        pygame.display.set_caption(self.title)

        self.running = True

        self.state = S_MAIN_MENU

        while self.running:
            self.update()
            self.render()

            pygame.display.update()
            self.fps_clock.tick(TARGET_FPS)

        logging.debug("stopping")
        pygame.mouse.set_visible(True)
        pygame.quit()
        sys.exit()

    def transition_states(self, old, new):
        self.state = new


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    g = Game()
    g.run()
