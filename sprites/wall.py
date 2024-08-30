import pygame as pg

from settings import *


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        # set the position of the wall, doesn't
        # change so there is no update function
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
