import os
from settings import GRIDWIDTH, GRIDHEIGHT
from map import Map

width, height = 10, 10
map_filename = 'random_map.txt'
gamemap = Map()
game_map = gamemap.generate_valid_map(int(GRIDWIDTH), int(GRIDHEIGHT))

entries = os.listdir("maps")
file_count = sum(os.path.isfile(os.path.join("maps", entry)) for entry in entries)

gamemap.save_map_to_file(game_map, f"maps/random_map_{file_count}.txt")
