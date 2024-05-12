from typing import TYPE_CHECKING
import items
from entity import Entity, Player, Enemy

if TYPE_CHECKING:
    from entity import Entity


class Action:
    def __init__(self, name: str, hotkey: str):
        self.name = name
        self.hotkey = hotkey

    def perform(self, entity: Entity) -> None:
        """Perform this action with the objects needed to determine its scope.

        `entity` is the object performing the action.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()

    def __str__(self):
        return f'{self.hotkey}'


class MovementAction(Action):
    """Action subclass that dictates entity movement"""
    def __init__(self, dx: int, dy: int):
        super().__init__(name='Movement', hotkey='None')

        self.dx = dx
        self.dy = dy

    def perform(self, entity: Entity) -> None:
        entity.x += self.dx
        entity.y += self.dy


class MoveNorth(MovementAction):
    def __init__(self):
        super().__init__(dx=0, dy=-1)
        self.name = 'Move North'
        self.hotkey = 'n'


class MoveSouth(MovementAction):
    def __init__(self):
        super().__init__(dx=0, dy=1)
        self.name = 'Move South'
        self.hotkey = 's'


class MoveEast(MovementAction):
    def __init__(self):
        super().__init__(dx=1, dy=0)
        self.name = 'Move East'
        self.hotkey = 'e'


class MoveWest(MovementAction):
    def __init__(self):
        super().__init__(dx=-1, dy=0)
        self.name = 'Move West'
        self.hotkey = 'w'


class ViewInventory(Action):
    """Prints the player's inventory"""

    def __init__(self):
        super().__init__(name='View inventory', hotkey='i')

    def perform(self, player: Player) -> None:
        for i in player.inventory:
            print(i)


class Attack(Action):
    def __init__(self, enemy: Enemy):
        super().__init__(name='Attack', hotkey='a')
        self.enemy = enemy

    def perform(self, player: Player) -> None:
        best_weapon = None
        max_dmg = 0
        for i in player.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print(f"You use {best_weapon.name} against {self.enemy.name}!")
        self.enemy.hp -= best_weapon.damage
        if not self.enemy.is_alive():
            print(f"You killed {self.enemy.name}!")
        else:
            print(f"{self.enemy.name} HP is {self.enemy.hp}.")





