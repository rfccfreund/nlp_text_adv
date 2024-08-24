import items
from action import Attack, ViewInventory, Flee, Interact
from entity_maker import *


class MapTile:
    def __init__(self, x, y):
        self.enemies = []
        self.explored = False
        self.interacted = False
        self.navigable = True
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def explore_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def is_explored(self):
        return self.explored

    def explore_room(self):
        self.explored = True

    def is_interacted(self):
        return self.interacted

    def is_navigable(self):
        return self.navigable

    def available_actions(self):
        """Returns all of the available actions in this room"""
        moves = [ViewInventory()]

        if not self.is_interacted():
            moves.append(Interact())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        print("""
        You find yourself if a cave with a flickering torch on the wall.
        You can make out several paths, each equally dark and foreboding.
        """)

    def explore_text(self):
        print("""
        You remember this room. This is where you started.        
        """)

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
        if self.interacted:
            self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        pass

    def explore_text(self):
        pass

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
        Another unremarkable part of the cave. You must forge onwards to find the exit
        """)

    def explore_text(self):
        pass

    def modify_player(self, player):
        # Room has no action on player
        pass


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.spawn_enemy(GiantSpider)

    def intro_text(self):
        if self.enemies and self.explored is False:
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

    def explore_text(self):
        pass


class BanditRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.spawn_enemy(Bandit)

    def intro_text(self):
        if self.enemies and self.explored is False:
            print("""
            A bandit leaps from behind a rock and attacks you
            """)
        elif self.enemies:
            print("""
            the bandit tries to close the distance and stab you with a short sword
            """)
        else:
            print("""
            The bandit lays dead in a pool of his own blood
                        """)

    def explore_text(self):
        pass


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.spawn_enemy(Ogre)

    def intro_text(self):
        if self.enemies and self.explored is False:
            print("""
            You walk right into the sight line of an ogre. It raises it club to strike
            """)
        elif self.enemies:
            print("""
            You hear the cracking of bones as the tip of the club catches you while dodging
            """)
        else:
            print("""
            The mighty ogre is slain by your hand. If only someone was around to see it
                        """)

    def explore_text(self):
        pass


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        print("""
        You notice something shiny in the corner.
        It's a dagger! You pick it up
        """)

    def explore_text(self):
        pass


class BlockedPassage(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.navigable = False

    def intro_text(self):
        pass

    def explore_text(self):
        pass

    def modify_player(self, player):
        # Room has no action on player
        pass


# class GuardTreasureRoom(LootRoom, EnemyRoom):


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        print("""
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!

        Victory is yours!
        """)

    def explore_text(self):
        pass

    def modify_player(self, player):
        player.victory = True


class StairsUp(MapTile):
    def intro_text(self):
        print("""
        Rough stairs headed upwards are carved into the stone
        """)

    def explore_text(self):
        pass

    def modify_player(self, player):
        pass
