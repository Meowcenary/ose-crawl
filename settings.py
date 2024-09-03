"""
Settings for pygame used by game.py initialize
"""

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Ose Crawl Dev"
BGCOLOR = DARKGREY

# Base this on WIDTH and HEIGHT
# 16 will make a ton of tiles
# TILESIZE = 16
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
# Speed in tiles per move
BASE_PLAYER_SPEED = 1
