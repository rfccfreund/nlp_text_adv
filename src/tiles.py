import items
from action import Attack, ViewInventory
from entity_maker import GiantSpider


class MapTile:
    def __init__(self, x, y):
        self.enemies = []
        self.explored = False
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def available_actions(self):
        """Returns all of the available actions in this room"""
        moves = [ViewInventory()]

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def intro_text(self):
        pass

    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def intro_text(self):
        pass

    def __init__(self, x, y):
        super().__init__(x, y)

    def spawn_enemy(self, enemy):
        self.enemies.append(enemy.spawn(self.x, self.y))

    def modify_player(self, player):
        if self.enemies:
            total_damage = 0
            for i in self.enemies:
                player.hp -= i.damage
                total_damage += i.damage

            print(f"You lost {total_damage} health. You have {player.hp} health remaining")

    def available_actions(self):
        """Returns all of the available actions in this room"""
        if self.enemies:
            for i in self.enemies:
                moves = [Attack(i)]
        else:
            moves = []

        return moves


class EmptyCavePath(MapTile):
    def intro_text(self):
        print("""
        Another unremarkable part of the cave. You must forge onwards
        """)

    def modify_player(self, player):
        # Room has no action on player
        pass


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.spawn_enemy(GiantSpider)

    def intro_text(self):
        if self.enemies and self.explored is False:
            self.explored = True
            print("""
            A giant spider jump down from its web in front of you
            """)
        elif self.enemies:
            print("""
            The spider bares its fangs and lunges towards you
            """)
        else:
            print("""
            The corpse of a large spider lays in front of you
            """)


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        print("""
        You notice something shiny in the corner.
        It's a dagger! You pick it up
        """)


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        print("""
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!

        Victory is yours!
        """)

    def modify_player(self, player):
        player.victory = True