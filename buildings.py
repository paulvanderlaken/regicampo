from production import ProducerResourceFood


class Building(object):
    '''Generic building class'''
    __name = 'generic building'
    __health = 100

    def __init__(self, name=__name, health=__health):
        self.name = name
        self.health = health

    def build_at(self, tile):
        self.tile = tile

    def __repr__(self):
        return f'{self.name} on tile {self.tile.location}'


class Farm(Building, ProducerResourceFood):
    '''Farm building to produce food from crops'''

    __name = 'farm'
    __health = 50
    __amount = 6
    __capacity = 10

    def __init__(self, name=__name, health=__health, amount=__amount, capacity=__capacity):
        Building.__init__(self, name=name, health=health)
        ProducerResourceFood.__init__(self, amount=amount, capacity=capacity)
