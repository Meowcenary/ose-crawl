from pathlib import Path

import pygame as pg

from event_types import *
from sprites import MenuOption
from settings import *


class MapSelectView:
    """
    Class for drawing and updating the map select menu view of the game.
    """
    def __init__(self, font):
        height, width = 100, 300
        self.font = font
        # options on the menu that can be selected
        self.menu_option_sprites = pg.sprite.Group()
        self.menu_options = []
        self.create_menu_options(width, height, font)

        self.current_option_index = 0
        self.current_option = self.menu_options[self.current_option_index]
        self.current_option.toggle_active()

    def create_menu_options(self, width, height, font):
        path = Path("maps/")

        option_y = 1
        count = 0
        for entry in path.iterdir():
            if entry.is_file():
                menu_option = MenuOption(1, 1+(height+10)*count, width, height, False, font, entry.name, BUILD_MAP_FROM_FILE)
                self.menu_options.append(menu_option)
                self.menu_option_sprites.add(menu_option)
                count += 1

    def update(self):
        self.menu_option_sprites.update()

    def change_active_option(self, new_active_index):
        """
        Toggle current option off of active, switch to new active option, toggle that
        option to active
        """
        self.current_option.toggle_active()
        self.current_option = self.menu_options[new_active_index%len(self.menu_options)]
        self.current_option.toggle_active()

    def handle_event(self, event):
        """
        Handle input events for the start menu view
        """
        # Most events will be handld by the view they're in, but sometimes things will
        # bubble up to the top level game class such as quitting the game or changing the
        # current view
        game_event = None

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                # this will need to be replaced with something more robust
                game_event = QUIT
            if event.key in (pg.K_UP, pg.K_k):
                self.current_option_index -= 1
                self.change_active_option(self.current_option_index)
            if event.key in (pg.K_DOWN, pg.K_j):
                self.current_option_index += 1
                self.change_active_option(self.current_option_index)
            if event.key in (pg.K_RETURN, pg.K_KP_ENTER):
                pg.event.post(pg.event.Event(self.current_option.on_select, map_file=self.current_option.text))

        return game_event

    def draw(self, screen):
        """
        Draw the menu to the screen.
        """
        # clear the screen
        screen.fill(BGCOLOR)

        # Dra the individual menu options
        for menu_option in self.menu_options:
            menu_option.draw(screen)
