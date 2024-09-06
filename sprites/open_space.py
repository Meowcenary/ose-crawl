from os import path

import pygame as pg

from settings import *


class OpenSpace(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.loaded_image = pg.image.load(path.join('images', 'dungeon_floor.png')).convert_alpha()

        # Surface is pygame object for representing images
        # setting self.image and self.rect allows calls to pygame.Group.draw()
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.blit(self.loaded_image, (0, 0))
        pg.transform.smoothscale(self.loaded_image, self.image.get_size(), dest_surface=self.image)

        self.rect = self.image.get_rect()
        self.x, self.y = x, y

        # set the position of the wall, doesn't
        # change so there is no update function
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
