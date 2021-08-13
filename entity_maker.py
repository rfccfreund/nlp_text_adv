
from entity import Entity, Enemy

"""
Using the enemy subclass we can create several different enemies without creating their own classes
The spawn function from entity will be used to place creatures in the World object 
"""
GiantSpider = Enemy(name="Giant Spider", hp=15, damage=2)

Ogre = Enemy(name="Ogre", hp=30, damage=15)

Bandit = Enemy(name="Bandit", hp=10, damage=1)




