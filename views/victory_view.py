import sys
from os import path

import pygame as pg

from event_types import *
from sprites import MenuOption
from settings import *


class VictoryView:
    """
    Class for drawing and updating the victory view of the game.
    """
    def __init__(self, font):
        self.font = font

    def handle_event(self, event):
        game_event = None

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                # this will need to be replaced with something more robust
                game_event = QUIT

        return game_event

    def update(self):
        pass

    def draw(self, screen):
        """
        Draw the view to the screen.
        """
        # clear the screen
        screen.fill(BGCOLOR)
        text_surface = self.font.render("Congratulations! You've found the exit.", False, (0, 0, 0))
        center_of_screen = (WIDTH/2, HEIGHT/2)
        screen.blit(text_surface, text_surface.get_rect(center=center_of_screen))
