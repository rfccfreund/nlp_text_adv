from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from world import World

T = TypeVar("T", bound="Entity")


class Entity:
    """
    A generic object to represent players, enemies, items, etc
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

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
