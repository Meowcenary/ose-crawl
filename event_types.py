"""
Custom event types for game
"""

import pygame as pg

# Change view events
CHANGE_VIEW_MAP = pg.event.custom_type()
CHANGE_VIEW_MAP_SELECT = pg.event.custom_type()
CHANGE_VIEW_START_MENU = pg.event.custom_type()
CHANGE_VIEW_VICTORY = pg.event.custom_type()

# Player events
PLAYER_PICKUP_GOLD = pg.event.custom_type()

# Game events
BUILD_MAP_FROM_FILE = pg.event.custom_type()
QUIT = pg.event.custom_type()
