from units import Unit
from production import ProducerResourceFood, ProducerUnitSoldier


class Building(Unit):
    '''Generic building class based on the unit class'''

    def __init__(self, **kwargs):
        Unit.__init__(self, **kwargs)

    def __repr__(self):
        return f'{self.name} built at tile {self.tile.location}'


class Farm(Building, ProducerResourceFood):
    '''Farm building to produce food from crops'''

    __name = 'farm'
    __health = 50
    __amount = 6
    __capacity = 50

    def __init__(self, name=__name, health=__health, amount=__amount, capacity=__capacity):
        Building.__init__(self, name=name, health=health)
        ProducerResourceFood.__init__(self, amount=amount, capacity=capacity)


class Barracks(Building, ProducerUnitSoldier):
    '''Barracks building to produce soldier units'''

    __name = 'barracks'
    __health = 500
    __amount = 1
    __capacity = 8

    def __init__(self, name=__name, health=__health, amount=__amount, capacity=__capacity):
        Building.__init__(self, name=name, health=health)
        ProducerUnitSoldier.__init__(self, amount=amount, capacity=capacity)
