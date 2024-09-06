from os import path

import pygame as pg

from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.loaded_image = pg.image.load(path.join('images', 'player.png')).convert_alpha()
        # Surface is pygame object for representing images
        # setting self.image and self.rect allows calls to pygame.Group.draw()
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.blit(self.loaded_image, (0, 0))
        pg.transform.smoothscale(self.loaded_image, self.image.get_size(), dest_surface=self.image)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x, self.y = x, y
        # the initial position is set by update

        self.gold_count = 0
        self.moves = 0

    def update(self):
        # Update the position of the image rect
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
