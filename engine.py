from entity import Player
from adventuretutorial.world import World
from rich import print
from rich.layout import Layout


class Engine:
    def __init__(self, world: World, player: Player):
        self.world = world
        self.player = player

    def set_up(self):
        self.player.set_location(self.world.starting_position)
        # These lines load the starting room and display the text
        room = self.world.tile_exists(self.player.x, self.player.y)
        print(room.intro_text())

    def begin(self):
        while self.player.is_alive() and not self.player.victory:
            room = self.world.tile_exists(self.player.x, self.player.y)
            # Moves through all the enemies in a room and removes dead ones
            for i in room.enemies:
                if not i.is_alive():
                    room.enemies.remove(i)
            # Prints room intro text
            room.intro_text()
            # Check again since the room could have changed the player's state
            room.modify_player(self.player)
            # Logic generates a list of actions the player can choose from
            if self.player.is_alive() and not self.player.victory:
                print("Choose an action:\n")
                # Prevents movement actions if an enemy is in the room
                if not room.enemies:
                    available_actions = self.world.adjacent_moves(room)
                else:
                    available_actions = []
                # modifies available actions for a player based on a rooms properties
                available_actions += room.available_actions()

                for action in available_actions:
                    print(action)
                action_input = input('Action: ')
                for action in available_actions:
                    if action_input == action.hotkey:
                        self.player.do_action(action)
                        break
