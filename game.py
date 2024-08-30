import sys
from os import path

import pygame as pg

from settings import *
from views import MapView
from sprites import Player, Wall

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        # Create blank map
        self.map_view = MapView()
        # Create a new player
        self.player = Player(1, 4)
        # self.current_view = None

    def new(self):
        """
        Build game objects, assign initial view
        """
        # Build the map - i.e put down walls and other map objects
        self.map_view.build()
        self.map_view.add_object(self.player)
        # Create a player and add it to the map
        # self.map_view.add_object(self.player)

    # game loop - set self.playing = False to end the game
    def run(self):
        self.playing = True
        while self.playing:
            # deltatime, the clock.tick(FPS) limits frame rate to FPS but also
            # returns the milliseconds that have passed since the last call
            self.dt = self.clock.tick(FPS) / 1000
            # process events
            self.events()
            # update sprite properties
            self.update()
            # draw grid and sprites on to the screen
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    # catch and handle all events here
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            # handle keyboard input
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # raise a quit event
                    self.quit()
                # handle movement keys arrow or hjkl
                if event.key in (pg.K_LEFT, pg.K_h):
                    self.map_view.move_object(self.player, dx=-1)
                if event.key in (pg.K_RIGHT, pg.K_l):
                    self.map_view.move_object(self.player, dx=1)
                if event.key in (pg.K_UP, pg.K_k):
                    self.map_view.move_object(self.player, dy=-1)
                if event.key in (pg.K_DOWN, pg.K_j):
                    self.map_view.move_object(self.player, dy=1)

    def update(self):
        # self.current_view.update()
        self.map_view.update()

    def draw(self):
        # self.current_view.draw()
        self.map_view.draw(self.screen)
        pg.display.flip()
