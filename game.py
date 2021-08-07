from adventuretutorial.engine import Engine
from adventuretutorial.entity_maker import Player
from adventuretutorial.world import World


def play():
    world = World()
    player = Player(name="Hero", hp=100)

    engine = Engine(world, player)

    engine.set_up()
    engine.begin()


if __name__ == "__main__":
    play()
