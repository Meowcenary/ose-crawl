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
        self.gold_count = None
        self.move_count = None

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

        label = []
        label.append(self.font.render("Congratulations! You've found the exit.", False, (0, 0, 0)))
        label.append(self.font.render(f"Gold: {self.gold_count}", False, (0, 0, 0)))
        label.append(self.font.render(f"Moves: {self.move_count}", False, (0, 0, 0)))

        center_of_screen = (WIDTH/2, HEIGHT/2)

        for i in range(len(label)):
            # Create a new tuple to center this line
            line_center = (center_of_screen[0], center_of_screen[1] + i*30)
            screen.blit(label[i], label[i].get_rect(center=line_center))
