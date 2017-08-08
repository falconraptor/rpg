class Item:
    def __init__(self, name, weight=0.0):
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{}(name={}, weight={})'.format(self.__class__.__name__, self.name, self.weight)
