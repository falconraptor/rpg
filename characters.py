from items import Item
from stats import HealthStat, LevelStat, ManaStat, StaminaStat


class Character:
    def __init__(self, name):
        self.health = HealthStat()
        self.name = name
        self.mana = ManaStat()
        self.stamina = StaminaStat()
        self.level = LevelStat()
        self.inventory = Inventory()

    def __getitem__(self, item):
        if hasattr(self, item):
            return self.__getattribute__(item)
        raise AttributeError('Attribute \'{}\' not defined'.format(item))


class Inventory:
    def __init__(self, max_space=10, max_weight=10, items=None):
        self.max_space = max_space
        self.max_weight = max_weight
        self.items = [i for i in items if isinstance(i, Item)] if items else []

    @property
    def max_space(self):
        return self.max_space

    @max_space.setter
    def max_space(self, max_space):
        self.max_space = 0 if max_space < 0 else max_space

    @property
    def max_weight(self):
        return self.max_weight

    @max_weight.setter
    def max_weight(self, max_weight):
        self.max_weight = 0 if max_weight < 0 else max_weight

    @property
    def items(self):
        return self.items

    @items.setter
    def items(self, items):
        if len(items) > self.max_space:
            raise ValueError("Not enough space available to replace the inventory.")
        for item in items:
            if not isinstance(item, Item):
                raise TypeError('This item is not a Item: {}'.format(item))
        self.items = items

    def weight(self):
        """Returns the amount of weight in the inventory."""
        return sum(item.weight for item in self.items)

    def weight_available(self):
        """Returns the amount of that can be added to the inventory"""
        return self.max_weight - self.weight()

    def space_available(self):
        """Returns the amount of empty space in the inventory."""
        return self.max_space - self.space_used()

    def space_used(self):
        """Returns the amount of space used in the inventory"""
        return len(self.items)

    def insert_items(self, items):
        """Adds item(s) to the inventory"""
        if not isinstance(items, iter):
            items = [items]
        for item in items:
            if not isinstance(item, Item):
                raise TypeError('This item is not a Item: {}'.format(item))
            if self.space_available():
                if self.weight_available() < item.weight:
                    self.items.append(item)
                else:
                    raise ValueError("Unable to carry that much weight")
            else:
                raise ValueError("Not enough space available in the inventory to add this item: {}".format(item))
