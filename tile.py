from buildings import Farm


class Tile(object):
    '''Basic board game tile'''

    def __init__(self,
                 location={'x': 0, 'y': 0},
                 type='generic',
                 resources=None,
                 sites=0,
                 buildings=[],
                 allows_movement=True):
        self.location = location
        self.tile_type = type
        self.resources = resources
        self.sites = sites
        self.buildings = buildings
        self.allows_movement = allows_movement

    def build(self, building):
        if self.has_available_site():
            self.buildings.append(building)
            building.build_at(self)
            print(f'Built {building}')
        else:
            print('No available sites')

    def has_available_site(self):
        return self.sites > 0 and self.sites > len(self.buildings)

    def __print_sites(self):
        site_name = 'building site'
        return f'1 {site_name}' if self.sites == 1 else f'{self.sites} {site_name}s'

    def __repr__(self):
        tile = f'{self.tile_type} tile'
        sites = f', with {self.__print_sites()}'
        return tile + sites


class Plain(Tile):
    '''
    Tile that allows
    * movement
    * buildings
    * food farming
    '''
    __tile_type = 'plain'
    __resources = 'food'
    __sites = 1

    def __init__(self, type=__tile_type, resources=__resources, sites=__sites):
        Tile.__init__(self, type=type, resources=resources, sites=sites)


class Forest(Tile):
    '''
    Tile that allows
    * movement
    * food foraging
    * wood cutting
    '''
    __tile_type = 'forest'
    __resources = ['food', 'lumber']
    __sites = 1

    def __init__(self, type=__tile_type, resources=__resources, sites=__sites):
        Tile.__init__(self, type=type, resources=resources, sites=sites)


class Mountain(Tile):
    '''
    Tile that allows
    * stone mining
    '''
    __tile_type = 'mountain'
    __resources = 'stone'
    __sites = 1
    __allows_movement = False

    def __init__(self, type=__tile_type, resources=__resources, sites=__sites, allows_movement=__allows_movement):
        Tile.__init__(self, type=type, resources=resources, sites=sites, allows_movement=allows_movement)


t1 = Plain()
print(t1.buildings)
print(t1.sites)
print(t1.has_available_site())

t1.build(Farm())

print(t1.buildings)
print(t1.sites)
print(t1.has_available_site())

[building.produce() for building in t1.buildings]
[building.produce() for building in t1.buildings]
[print(building.storage) for building in t1.buildings]
