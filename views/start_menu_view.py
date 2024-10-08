import pygame as pg

from event_types import *
from sprites import MenuOption
from settings import *


class StartMenuView:
    """
    Class for drawing and updating the start menu view of the game.
    """
    def __init__(self, font):
        height, width = 100, 340
        self.font = font
        # options on the menu that can be selected
        self.menu_option_sprites = pg.sprite.Group()
        self.menu_options = [
            MenuOption(1, 1, width, height, True, font, "Start New Game", CHANGE_VIEW_MAP),
            MenuOption(1, height+10, width, height, False, font, "View High Scores"),
            MenuOption(1, (height+10)*2, width, height, False, font, "Map Select", CHANGE_VIEW_MAP_SELECT),
            MenuOption(1, (height+10)*3, width, height, False, font, "Generate Random Map", BUILD_RANDOM_MAP)
        ]
        self.menu_option_sprites.add(self.menu_options[0])
        self.menu_option_sprites.add(self.menu_options[1])
        self.menu_option_sprites.add(self.menu_options[2])
        self.menu_option_sprites.add(self.menu_options[3])
        self.current_option_index = 0
        self.current_option = self.menu_options[self.current_option_index]

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
                game_event = self.current_option.on_select

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
