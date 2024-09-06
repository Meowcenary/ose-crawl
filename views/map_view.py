import sys
from os import path

import pygame as pg

from event_types import *
from settings import *
from sprites import GoalTile, Gold, OpenSpace, Wall


class MapView:
    """
    Class for drawing and updating the map view of the game
    """
    def __init__(self, player):
        self.map_objects = pg.sprite.Group()
        # Specific group for walls
        self.walls = pg.sprite.Group()
        self.open_spaces = pg.sprite.Group()
        self.goal_tile = pg.sprite.Group()
        self.player = player

    def build(self):#filepath=""):
        """
        WIP

        Determine if building from file or generating and populate the map
        """
        self.load_map_from_file()

    def handle_event(self, event):
        """
        Handle input events for the map view
        """
        # Most events will be handld by the view they're in, but sometimes things will
        # bubble up to the top level game class such as quitting the game or changing the
        # current view
        game_event = None

        if event.type == CHANGE_VIEW_VICTORY:
            game_event = CHANGE_VIEW_VICTORY

        if event.type == PLAYER_PICKUP_GOLD:
          event.gold.kill()
          self.player.gold_count += 1

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                # this will need to be replaced with something more robust
                game_event = CHANGE_VIEW_START_MENU
            # handle movement keys arrow or hjkl
            if event.key in (pg.K_LEFT, pg.K_h):
                if self.move_object(self.player, dx=-1):
                    self.player.moves += 1
            if event.key in (pg.K_RIGHT, pg.K_l):
                if self.move_object(self.player, dx=1):
                    self.player.moves += 1
            if event.key in (pg.K_UP, pg.K_k):
                if self.move_object(self.player, dy=-1):
                    self.player.moves += 1
            if event.key in (pg.K_DOWN, pg.K_j):
                if self.move_object(self.player, dy=1):
                    self.player.moves += 1

        return game_event

    def update(self):
        self.map_objects.update()

    def draw(self, screen):
        """
        Draw the map to the screen. Redraws map each time
        """
        screen.fill(BGCOLOR)
        self.walls.draw(screen)
        self.open_spaces.draw(screen)
        self.goal_tile.draw(screen)
        self.map_objects.draw(screen)

    def draw_grid(self, screen):
        """
        Draw the background grid for the game
        """
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(screen, LIGHTGREY, (0, y), (WIDTH, y))

    def add_object(self, map_object):
        """
        Add a map object, something that can be moved or removed from the map (i.e not
        walls)
        """
        self.map_objects.add(map_object)

    def move_object(self, map_object, dx=0, dy=0):
        """
        Move a map object to a new position where dx is the change in x and dy is the
        change in y
        """
        # TODO: Refactor so that map bojects implement move functions themselves for
        # containing logic on what they can and can't hit
        # map_object.move(dx, dy)

        # Player specific logic for moving
        if self.not_collide_with_walls(map_object, dx, dy):
            map_object.x += dx
            map_object.y += dy
        else:
            return False

        if self.collide_with_goal_tile(map_object):
            pg.event.post(pg.event.Event(CHANGE_VIEW_VICTORY))

        collides, gold = self.collide_with_gold(map_object)
        if gold:
            pg.event.post(pg.event.Event(PLAYER_PICKUP_GOLD, gold=gold))

        return True

    # If you reverse this logic so that on collision it returns True and on miss False
    # you can do a kind of cool climb on walls movement
    def not_collide_with_walls(self, map_object, dx=0, dy=0):
        """
        Determine if a game object will collide with a wall
        """
        for wall in self.walls:
            if wall.x == map_object.x + dx and wall.y == map_object.y + dy:
                return False
        return True

    def collide_with_goal_tile(self, map_object, dx=0, dy=0):
        """
        Determine if a game object collides with the goal tile
        """
        for gt in self.goal_tile:
            if gt.x == map_object.x + dx and gt.y == map_object.y + dy:
                return True
        return False

    # For an object to be picked up, set collision to only detect after the player has
    # moved onto the sprite i.e wait set dx , dy to zero so it doesn't look at the space
    # the player is moving into, but the one it's on
    def collide_with_gold(self, map_object, dx=0, dy=0):
        for map_obj in self.map_objects:
            if type(map_obj) == Gold and map_obj.x == map_object.x + dx and map_obj.y == map_object.y + dy:
                return True, map_obj
        return False, None

    def add_room(self, top_left, bottom_right):
        """
        Add an enclosed room to the map. from top left coordinate to bottom right
        coordinate
        """
        top_left_x, top_left_y = top_left[0], top_left[1]
        bottom_right_x, bottom_right_y = bottom_right[0], bottom_right[1]
        # top
        self.add_h_wall(top_left_x, bottom_right_x, top_left_y)
        # left
        self.add_v_wall(top_left_y, bottom_right_y, top_left_x)
        # right, either right or bottom needs + 1 to extend
        self.add_v_wall(top_left_y, bottom_right_y+1, bottom_right[0])
        # bottom
        self.add_h_wall(top_left_x, bottom_right_x, bottom_right[1])

    def add_h_wall(self, start_x, end_x, y):
        """
        Add a horizontal wall from column start_x to column end_x that is on row y
        """
        for x in range(start_x, end_x):
            self.walls.add(Wall(self, x, y))

    def add_v_wall(self, start_y, end_y, x):
        """
        Add a vertical wall from row start_y to row end_y that is on column x
        """
        for y in range(start_y, end_y):
            self.walls.add(Wall(x, y))

    def load_map_from_file(self, file='map.txt'):
        """
        Load a map from a formatted text file
        """
        game_folder = path.join(path.dirname(__file__), '..')
        map_data = []

        # open map.txt and read each line of it into map_data
        with open(path.join(game_folder, 'maps', file), 'rt') as f:
            for line in f:
                map_data.append(line)

        for row, tiles in enumerate(map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.walls.add(Wall(col, row))
                elif tile == 'X':
                    self.goal_tile.add(GoalTile(col, row))
                elif tile == 'G':
                    self.map_objects.add(Gold(col, row))
                    self.open_spaces.add(OpenSpace(col, row))
                elif tile == '.' or tile == 'P':
                    self.open_spaces.add(OpenSpace(col, row))
