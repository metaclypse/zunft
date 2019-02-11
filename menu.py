import pygame
import sys
from game_utils import load_image
import game
import datetime
import logging

class ButtonListener(object):
    def __init__(self):
        pass

    def update(self):
        pass


class Button(pygame.sprite.Sprite):
    def __init__(self, game, start_pos, function, text, minimum_size=-1):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.listeners = []

        # Create text
        self.text = text
        button_font = pygame.font.SysFont("Alex_Elegant", 18, bold=True)
        label = button_font.render(text, 1, (255, 255, 255))
        text_width, text_height = button_font.size(text)

        # Set up images & arrange
        left_image, lr = load_image("btn_corner.png")
        right_image, rr = load_image("btn_corner.png")
        right_image = pygame.transform.flip(right_image, True, False)
        center_image, cr = load_image("btn_middle.png")

        size = (text_width / cr.size[0]) + 1
        if size < minimum_size:
            size = minimum_size

        target_width = lr.size[0] + cr.size[0] * size + rr.size[0]
        target_height = lr.size[1]

        # Create image and blit parts onto it
        self.image = pygame.Surface((target_width, target_height))

        self.image.blit(left_image, (0, 0))
        next_x = lr.size[0]

        for i in range(0, size):
            self.image.blit(center_image, (next_x, 0))
            next_x += cr.size[0]

        self.image.blit(right_image, (next_x, 0))

        # Blit text to the image
        text_x = (target_width / 2) - (text_width / 2)
        text_y = (target_height / 2) - (text_height / 2)

        self.image.blit(label, (text_x, text_y))

        self.image = self.image.convert_alpha()

        # Set up the rest
        self.rect = self.image.get_rect()
        self.pos = start_pos
        self.rect.left, self.rect.top = self.pos
        self.function = function

    def register_listener(self, listener):
        self.listeners += listener

    def notify_listeners(self):
        for l in self.listeners:
            l.update()

    def update(self):
        self.rect.left, self.rect.top = self.pos

    def call_function(self):
        if not (self.function is None):
            self.button_function()

    def button_function(self):
        print("(" + str(datetime.datetime.now()) +") Clicked button with text: \"" + self.text + "\"")


class NewMatchButton(Button):
    def button_function(self):
        self.game.start_game_setup()


class EndGameButton(Button):
    def button_function(self):
        logging.debug("main menu: ending game")
        self.game.schedule_state_change(game.S_QUIT)


class MainMenu:
    def __init__(self, game, offset=(0, 0)):
        self.game = game

        self.button_new_game = NewMatchButton(game, (0 + offset[0], 0 + offset[1]), self.new_game, "Neues Spiel", 15)
        self.button_load_game = Button(game, (0 + offset[0], 50 + offset[1]), self.load_game, "Spiel laden", 15)
        self.button_settings = Button(game, (0 + offset[0], 100 + offset[1]), self.settings, "Einstellungen", 15)
        self.button_quit = EndGameButton(game, (0 + offset[0], 150 + offset[1]), self.quit, "Spiel beenden", 15)

        self.game.all_sprites.add(self.button_new_game, self.button_load_game, self.button_settings, self.button_quit)

    def new_game(self):
        pass

    def load_game(self):
        pass

    def settings(self):
        pass

    def quit(self):
        pass