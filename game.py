#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

import person
import menu

reload(sys)
sys.setdefaultencoding('utf8')

S_INIT = 0
S_MENU = 1
S_SETUP = 2
S_MATCH = 3
S_TRANSITION = 4

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

    def update(self):
        self.all_sprites.update()

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
        print("starting")

        pygame.init()
        pygame.mouse.set_visible(False)
        self.fps_clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(self.title)

        self.running = True

        def tst():
            print("BUUUUHHH")
        test_btn = menu.Button((200, 200), tst, "Ey du Mungo!!")
        test_btn.add(self.all_sprites)

        text_btn2 = menu.Button((200, 250), tst, "Wasn ey, komm doch her!")
        text_btn2.add(self.all_sprites)

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == MOUSEMOTION:
                    self.mouse_x, self.mouse_y = event.pos
                elif event.type == MOUSEBUTTONUP:
                    self.mouse_x, self.mouse_y = event.pos
                    print("click")
                    for s in self.all_sprites:
                         if s.rect.collidepoint((self.mouse_x, self.mouse_y)) and isinstance(s, menu.Button):
                             s.call_function()

                elif event.type == MOUSEBUTTONDOWN:
                    self.mouse_x, self.mouse_y = event.pos
                    self.click_down = True
                elif event.type == KEYDOWN:
                    if event.key == K_a:
                        print("A was pressed")
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))

            self.render()

            pygame.display.update()
            self.fps_clock.tick(TARGET_FPS)

        print("stopping")
        pygame.mouse.set_visible(True)
        pygame.quit()
        sys.exit()

    def transition_states(self, old, new):
        self.state = new

if __name__ == "__main__":
    g = Game()
    g.run()
