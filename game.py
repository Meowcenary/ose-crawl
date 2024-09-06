import sys
from os import path

import pygame as pg

from event_types import *
from settings import *
from sprites import Player, Wall
from views import MapView, StartMenuView, VictoryView

class Game:
    def __init__(self):
        """
        Initialize PyGame settings and create game specific objects.
        """
        # Pygame settings
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        # Potentially break this out to settings FONT='Comic Sans MS', FONT_SIZE=30
        self.comic_sans_font = pg.font.SysFont('Comic Sans MS', 30)

        # Create a new player
        self.player = Player(1, 4)

        # Create views
        self.map_view = MapView(self.player)
        self.start_menu_view = StartMenuView(self.comic_sans_font)
        self.victory_view = VictoryView(self.comic_sans_font)

        # Set initial view
        self.current_view = self.start_menu_view

    def new(self):
        """
        Build game objects, assign initial view
        """
        # Build the map - i.e put down walls and other map objects
        self.map_view.build()
        self.map_view.add_object(self.player)

    def run(self):
        """
        Game loop for program.

        Handle events, update sprites, draw to screen.
        """
        while True:
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
        """
        Signal PyGame to quit.
        """
        pg.quit()
        sys.exit()

    # catch and handle all events here
    def events(self):
        """
        Process events and handle any that bubble up from view.
        """
        for event in pg.event.get():
            # game events are signals from views that tell the game that to handle the
            # event it will require the game class to step in e.g quitting the game,
            # switching views
            game_event = self.current_view.handle_event(event)

            if game_event == CHANGE_VIEW_MAP:
                self.set_current_view(self.map_view)
            if game_event == CHANGE_VIEW_START_MENU:
                self.set_current_view(self.start_menu_view)
            if game_event == CHANGE_VIEW_VICTORY:
                self.victory_view.gold_count, self.victory_view.move_count = self.player.gold_count, self.player.moves
                self.set_current_view(self.victory_view)
            if game_event == QUIT:
                self.quit()

    def set_current_view(self, current_view=None):
        """
        Set the current view for the game.
        """
        self.current_view = current_view

    def update(self):
        """
        Update all the sprites on the current view.
        """
        self.current_view.update()

    def draw(self):
        """
        Draw the current view to the screen and render with display.flip().
        """
        self.current_view.draw(self.screen)
        pg.display.flip()
