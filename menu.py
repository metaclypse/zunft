import pygame
from game_utils import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, start_pos, function, text):
        pygame.sprite.Sprite.__init__(self)

        size = len(text)

        left_image, lr = load_image("btn_left.png")
        right_image, rr = load_image("btn_right.png")
        center_image, cr = load_image("btn_middle.png")

        target_width = lr.size[0] + cr.size[0] * size + rr.size[0]
        target_height = lr.size[1]

        self.image = pygame.Surface((target_width, target_height))

        self.image.blit(left_image, (0, 0))
        next_x = lr.size[0]

        for i in range(0, size):
            self.image.blit(center_image, (next_x, 0))
            next_x += cr.size[0]

        self.image.blit(right_image, (next_x, 0))

        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.function = function

    def update(self):
        pass

    def call_function(self):
        if not self.function is None:
            self.function()


class MainMenu:
    def __init__(self, game):
        self.game = game
