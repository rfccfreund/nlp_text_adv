from adventuretutorial import action


class World:
    def __init__(self):
        self._world = {}
        self.starting_position = [0, 0]
        self.entities = []

        # Parses a file that describes the world space into the _world object
        with open('resources/map.txt', 'r') as f:
            rows = f.readlines()
        x_max = len(rows[0].split(','))  # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split(',')
            for x in range(x_max):
                tile_name = cols[x].replace('\n', '')
                if tile_name == 'StartingRoom':
                    self.starting_position = [x, y]
                self._world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

    def adjacent_moves(self, tile):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if self.tile_exists(tile.x + 1, tile.y):
            moves.append(action.MoveEast())
        if self.tile_exists(tile.x - 1, tile.y):
            moves.append(action.MoveWest())
        if self.tile_exists(tile.x, tile.y + 1):
            moves.append(action.MoveSouth())
        if self.tile_exists(tile.x, tile.y - 1):
            moves.append(action.MoveNorth())
        return moves

    def tile_exists(self, x, y):
        return self._world.get((x, y))
