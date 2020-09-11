# Boilerplate
import pygame as pg
import sys
from os import path
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []

        # open map.txt and read each line of it into map_data
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
# Boilerplate end

    # initialize all variables and do all the setup for a new game
    def new(self):
        # all_sprites and walls are set to an empty sprite group
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        # 0,0 is top left corner
        # create and render a player sprite
        self.player = Player(self, 10, 10)

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)

        # Room in top left corner
        # self.draw_room((0, 0), (6, 7))
        # hallway connecting left and right room
        # self.draw_room((6, 5), (10, 7))
        # room to the right, not very tall
        # self.draw_room((10, 3), (22, 7))

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

    def update(self):
        # calling update on a sprite group will call update on
        # all of the sprites within the group
        self.all_sprites.update()

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
                    self.player.move(dx=-1)
                if event.key in (pg.K_RIGHT, pg.K_l):
                    self.player.move(dx=1)
                if event.key in (pg.K_UP, pg.K_k):
                    self.player.move(dy=-1)
                if event.key in (pg.K_DOWN, pg.K_j):
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# drawing functions
    def draw(self):
        # screen is a surface, make it entirely one color
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        # this will call draw on each sprite in the group
        # might be able to just draw the player?
        self.all_sprites.draw(self.screen)

        # Update the full display Surface to the screen
        pg.display.flip()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_room(self, start, end):
        start_x, start_y = start[0], start[1]
        end_x, end_y = end[0], end[1]
        # top
        self.draw_h_wall(start_x, end_x, start_y)
        # left
        self.draw_v_wall(start_y, end_y, start_x)
        # right, either right or bottom needs + 1 to extend
        self.draw_v_wall(start_y, end_y+1, end[0])
        # bottom
        self.draw_h_wall(start_x, end_x, end[1])

    def draw_h_wall(self, start_x, end_x, y):
        for x in range(start_x, end_x):
            Wall(self, x, y)

    def draw_v_wall(self, start_y, end_y, x):
        for y in range(start_y, end_y):
            Wall(self, x, y)
