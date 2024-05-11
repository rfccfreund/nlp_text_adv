from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING
import items

if TYPE_CHECKING:
    from world import World

T = TypeVar("T", bound="Entity")


class Entity:
    """
    A generic object to represent players, enemies, etc
    """

    def __init__(
            self,
            x: int = 0,
            y: int = 0,
            name: str = "<Unnamed>",
            hp: int = 0
    ):
        self.hp = hp
        self.x = x
        self.y = y
        self.name = name

    def spawn(self: T, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        return clone


class Enemy(Entity):
    """
    Subclass of Entity used to create various monsters for our hero to fight
    """

    def __init__(self, name: str, hp: int, damage: int, **kwargs):
        super().__init__(name=name, hp=hp, **kwargs)
        self.damage = damage

    def is_alive(self) -> bool:
        return self.hp > 0


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

    def do_action(self, action: [], **kwargs):
        action.perform(self, **kwargs)
