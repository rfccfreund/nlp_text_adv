from adventuretutorial.entity_maker import Player
from adventuretutorial.tiles import EnemyRoom
from adventuretutorial.world import World


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
            for i in room.enemies:
                if not i.is_alive():
                    room.enemies.remove(i)
            room.intro_text()
            room.modify_player(self.player)
            # Check again since the room could have changed the player's state
            if self.player.is_alive() and not self.player.victory:
                print("Choose an action:\n")
                available_actions = self.world.adjacent_moves(room)
                available_actions += room.available_actions()
                for action in available_actions:
                    print(action)
                action_input = input('Action: ')
                for action in available_actions:
                    if action_input == action.hotkey:
                        self.player.do_action(action, **action.kwargs)
                        break

