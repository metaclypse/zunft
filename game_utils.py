import os
import pygame

RLEACCEL = 16384


def load_image(filename):  # , colorkey=None):
    fullname = os.path.join("res", "img", filename)

    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message

    image = image.convert_alpha()
    # image = image.convert()

    # if colorkey is not None:
    #     if colorkey is -1:
    #         colorkey = image.get_at((0, 0))
    #     image.set_colorkey(colorkey, RLEACCEL)

    return image, image.get_rect()
