from entity import Player
import world
import player_input


class Engine:
    def __init__(self, world: world, player: Player):
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
            if not room.is_explored():
                room.explored()
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
                # Prevents movement actions if an enemy is in the room
                if not room.enemies:
                    available_actions = self.world.adjacent_moves(room)
                else:
                    available_actions = []
                # modifies available actions for a player based on a rooms properties
                available_actions += room.available_actions()
                available_actions += self.world.flee_move(room)

                directions = ""
                for x in self.world.adjacent_moves(room):
                    directions += ' ' + str(x)
                print("Available paths: " + directions)
                print('What would you like to do next?')
                line = [input()]
                player_choice = player_input.vectorizer.transform(line)
                action_input = player_input.classifier.predict(player_choice)
                action_input = action_input[0][0]
                for action in available_actions:
                    if action_input == action.hotkey:
                        self.player.do_action(action)
                        break
