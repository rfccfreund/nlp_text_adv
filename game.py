from engine import Engine
import world
import entity


def play():
    """
    A world object parses a csv to create a dict which
    stores tiles. World also stores the generic movement actions to navigate
    the dict
    """
    _world = world.World()
    """
    A player object is a subclass of a entity which differs by having an inventory
    """
    player = entity.Player(name="Hero", hp=100)

    """
    engine object contains the majority of the game logic and take a player object 
    and a world object
    """
    engine = Engine(_world, player)

    engine.set_up()
    engine.begin()


if __name__ == "__main__":
    play()
