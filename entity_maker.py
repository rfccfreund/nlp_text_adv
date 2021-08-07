from random import random

from adventuretutorial import items
from entity import Entity


class Enemy(Entity):
    """
    Subclass of Entity used to create various monsters for our hero to fight
    """

    def __init__(self, name: str, hp: int, damage: int, **kwargs):
        super().__init__(name=name, hp=hp, **kwargs)
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


"""
Using the enemy subclass we can create several different enemies without creating their own classes
The spawn function from entity will be used to place creatures in the World object 
"""
GiantSpider = Enemy(name="Giant Spider", hp=10, damage=2)

Ogre = Enemy(name="Ogre", hp=30, damage=15)


class Player(Entity):
    """
    Subclass of Entity which will be used to create our hero
    """

    def __init__(self, name: str, hp: int, inventory: [] = [items.Gold(15), items.Rock()], **kwargs):
        super().__init__(name=name, hp=hp, **kwargs)
        self.inventory = inventory
        self.victory = False

    def set_location(self, location):
        self.x = location[0]
        self.y = location[1]

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print(f"You use {best_weapon.name} against {enemy.name}!")
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        """Moves the player randomly to an adjacent"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
