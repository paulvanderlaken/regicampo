class Object:
    '''Generic class for any object in the game'''

    def __init__(self, name):
        self.name = name

    def create_at(self, tile):
        self.tile = tile

    def __repr__(self):
        return f'{self.name} on tile {self.tile.location}'


class Unit(Object):
    '''Generic unit class'''

    def __init__(self, health, **kwargs):
        Object.__init__(self, **kwargs)
        self.health = health


class Army(Unit):
    '''Generic army class'''

    def __init__(self,  **kwargs):
        Unit.__init__(self, **kwargs)

    def __repr__(self):
        return f'{self.name} stationed at tile {self.tile.location}'


class AttackerMelee:

    def __init__(self, damage):
        self.damage = damage

    def attack(self, other='test'):
        print(f'{self.name} does {self.damage} to {other}')


class Soldier(Unit, AttackerMelee):
    '''Soldier unit class'''

    __name = 'soldier'
    __health = 10
    __damage = 2

    def __init__(self, name=__name, health=__health, damage=__damage):
        Army.__init__(self, name=name, health=health)
        AttackerMelee.__init__(self, damage=damage)
