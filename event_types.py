"""
Custom event types for game
"""

import pygame as pg


CHANGE_VIEW_MAP = pg.event.custom_type()
CHANGE_VIEW_START_MENU = pg.event.custom_type()
CHANGE_VIEW_VICTORY = pg.event.custom_type()

CHANGE_VIEW = pg.event.custom_type()
QUIT = pg.event.custom_type()
