class Tile:
    '''Basic board game tile'''

    def __init__(self,
                 type='generic',
                 resources=None,
                 sites=0,
                 buildings=[],
                 allows_movement=True):
        self.tile_type = type
        self.resources = resources
        self.sites = sites
        self.buildings = buildings
        self.allows_movement = allows_movement

    def build(self, building):
        if self.has_available_site():
            self.buildings.append(building)
        else:
            print('No available sites')

    def has_available_site(self):
        return self.sites > 0 and self.sites < self.buildings

    def __repr__(self):
        tile = f'{self.tile_type} tile'
        sites = f', with {self.sites} site{"s" if self.sites > 1 else ""}' if self.sites > 0 else ''
        return tile + sites


class Plain(Tile):
    '''
    Tile that allows
    * movement
    * buildings
    * food farming
    '''

    def __init__(self, type='plain', resources='food', sites=1):
        super().__init__(type=type, resources=resources, sites=sites)


class Forest(Tile):
    '''
    Tile that allows
    * movement
    * food foraging
    * wood cutting
    '''

    def __init__(self, type='forest', resources=['food', 'lumber'], sites=1):
        super().__init__(type=type, resources=resources, sites=sites)


class Mountain(Tile):
    '''
    Tile that allows
    * stone mining
    '''

    def __init__(self):
        self.tile_type = 'mountain'
        self.resources = ['stone']
        self.building_site = None

    def __init__(self, type='mountain', resources='stone', sites=1, allows_movement=False):
        super().__init__(type=type, resources=resources, sites=sites, allows_movement=allows_movement)


t1 = Tile()
t2 = Plain()
t3 = Forest()
t4 = Mountain()

print(t1)
print(t2)
print(t3)
print(t4)
