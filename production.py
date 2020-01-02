class Producer(object):
    '''Generic production class. Outputs either a resource or a unit'''

    def __init__(self, product, amount=1, capacity=10):
        self.product = product
        self.amount = amount
        self.capacity = capacity
        self.storage = []  # start with empty storage

    def produce(self):
        output = [self.product for _ in range(self.amount)]
        print(f'{self} produced {output}')
        self.store(output)

    def store(self, products):
        [self.storage.append(p) for p in products if len(self.storage) < self.capacity]


class ProducerResource(Producer):
    '''Production of resources'''

    def __init__(self, **kwargs):
        Producer.__init__(self, **kwargs)


class ProducerResourceFood(ProducerResource):
    '''Production of food resources'''
    __product = 'food'

    def __init__(self, product=__product, **kwargs):
        ProducerResource.__init__(self, product=product, **kwargs)
