import pygame as pg
from settings import *

# inherits from Sprite class
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # all_sprites is a sprite.Group object
        self.groups = game.all_sprites
        # call parent class initialize function in order to extend functionality # of sprite class
        # https://stackoverflow.com/questions/16126734/what-is-the-purpose-of-calling-init-directly
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # Surface is pygame object for representing images
        # setting self.image and self.rect allows calls to pygame.Group.draw()
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        # get the rectangular area of the Surface
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        # the initial position is set by update

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        # Update the position of the image rect
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

# inherits from Sprite class
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # this block is almost exactly the same as Player __init__, but with
        # the fill being YELLOW and adding it to the sprite group game.walls
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        ###

        # set the position of the wall, doesn't
        # change so there is no update function
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
