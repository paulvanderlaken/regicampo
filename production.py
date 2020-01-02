from units import Soldier
from resources import ResourceFood


class Producer(object):
    '''Generic production class. Can produce both units and resources'''

    def __init__(self, product, amount=1, capacity=10):
        self.product = product
        self.amount = amount
        self.capacity = capacity
        self.storage = []  # start with empty storage

    def produce(self):
        output = [self.product for _ in range(self.amount)]
        for obj in output:
            obj.create_at(self.tile)
        print(f'{self} produced {output}')
        self.store(output)

    def store(self, products):
        [self.storage.append(p) for p in products if len(self.storage) < self.capacity]


class ProducerResource(Producer):
    '''Production of resources'''

    def __init__(self, **kwargs):
        Producer.__init__(self, **kwargs)


class ProducerUnit(Producer):
    '''Production of units'''

    def __init__(self, **kwargs):
        Producer.__init__(self, **kwargs)


class ProducerResourceFood(ProducerResource):
    '''Production of food resources'''
    __product = ResourceFood()

    def __init__(self, product=__product, **kwargs):
        ProducerResource.__init__(self, product=product, **kwargs)


class ProducerUnitSoldier(ProducerUnit):
    '''Production of soldier units'''
    __product = Soldier()

    def __init__(self, product=__product, **kwargs):
        ProducerUnit.__init__(self, product=product, **kwargs)
