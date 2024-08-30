import pygame as pg

from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # Surface is pygame object for representing images
        # setting self.image and self.rect allows calls to pygame.Group.draw()
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x, self.y = x, y
        # the initial position is set by update

    def update(self):
        # Update the position of the image rect
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
