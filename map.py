import os
from random import randint
from collections import deque
from settings import GRIDWIDTH, GRIDHEIGHT


class Map:
    """
    Class to generate a random map and save it to a file
    """
    def __init__(self):
        pass

    def generate_map(self, width, height):
        """
        Generate a random map that may or may not be solvable
        """
        # Initialize map with walls
        game_map = [['.' for _ in range(width)] for _ in range(height)]

        total_walls = width * height // 2 + width * height // 10
        # Place walls in roughly half the spaces
        for _ in range(total_walls):
            x, y = randint(0, width - 1), randint(0, height - 1)
            game_map[y][x] = '1'

        # Place goal and player start
        game_map[randint(height-3, height - 1)][randint(0, width - 1)] = 'X'
        game_map[1][4] = 'P'

        return game_map

    def is_solvable(self, game_map, start, goal):
        rows, cols = len(game_map), len(game_map[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Down, Left, Right
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            if current == goal:
                return True

            for direction in directions:
                next_row, next_col = current[0] + direction[0], current[1] + direction[1]
                if (0 <= next_row < rows and 0 <= next_col < cols and
                    (next_row, next_col) not in visited and
                    game_map[next_row][next_col] != '1'):

                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col))

        return False

    def generate_valid_map(self, width, height):
        """
        Generate random maps until a solvable map is created
        """
        while True:
            print("Making new map")
            game_map = self.generate_map(width, height)
            start, goal = None, None

            # Find start and goal positions
            for y in range(height):
                for x in range(width):
                    if game_map[y][x] == 'P':
                        start = (y, x)
                    elif game_map[y][x] == 'X':
                        goal = (y, x)
                    if start and goal:
                        break
                if start and goal:
                    break

            if start and goal and self.is_solvable(game_map, start, goal):
                return game_map

    def save_map_to_file(self, game_map, filename):
        with open(filename, 'w') as file:
            for row in game_map:
                file.write(''.join(row) + '\n')

    def build_valid_map(self):
        game_map = self.generate_valid_map(int(GRIDWIDTH), int(GRIDHEIGHT))

        entries = os.listdir("maps")
        file_count = sum(os.path.isfile(os.path.join("maps", entry)) for entry in entries)

        self.save_map_to_file(game_map, f"maps/random_map_{file_count}.txt")
