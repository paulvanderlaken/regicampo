from units import Object


class Resource(Object):
    '''Generic resources class'''

    def __init__(self, **kwargs):
        Object.__init__(self, **kwargs)


class ResourceFood(Resource):
    '''Food resource to be used for consumption'''

    __name = 'food'

    def __init__(self, name=__name):
        Object.__init__(self, name=name)
