import pygame
from game_utils import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, start_pos, function, text):
        pygame.sprite.Sprite.__init__(self)

        # Create text
        button_font = pygame.font.SysFont("monospace", 18, bold=True)
        label = button_font.render(text, 1, (255, 255, 255))
        text_width, text_height = button_font.size(text)

        # Set up images & arrange
        left_image, lr = load_image("btn_corner.png")
        right_image, rr = load_image("btn_corner.png")
        right_image = pygame.transform.flip(right_image, True, False)
        center_image, cr = load_image("btn_middle.png")

        size = (text_width / cr.size[0]) + 1

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

    def update(self):
        self.rect.left, self.rect.top = self.pos

    def call_function(self):
        if not self.function is None:
            self.function()


class MainMenu:
    def __init__(self, game):
        self.game = game
