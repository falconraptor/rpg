class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{}(name={})'.format(self.__class__.__name__, self.name)
