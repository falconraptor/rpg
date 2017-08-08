from secrets import randbelow

from items import Item
from stats import LevelStat


class Weapon(Item):
    def __init__(self, name, base_damage=1, max_damage=1, crit_chance=0, crit_bonus=.05, weight=1, level=None):
        super().__init__(name=name, weight=weight)
        self.base_damage = base_damage
        self.max_damage = max_damage
        self.crit_chance = crit_chance
        self.crit_bonus = crit_bonus
        self.level = LevelStat(level=1, max_xp=200, xp_rate=.5) if not level else level
        self.abilities = {}

    def __str__(self):
        return '[{}]: level: {}, damage: {}/{}, critical chance: {:.02%}, critical bonus: {:.02%}'.format(
            self.name, self.level.level, round(self.base_damage, 2), round(self.max_damage, 2), self.crit_chance,
            self.crit_bonus)

    def __repr__(self):
        return '{}(level={}, damage={}, max_damage={}, crit_chance={}, crit_bonus={})'.format(
            self.__class__.__name__, self.level, self.base_damage, self.max_damage, self.crit_chance, self.crit_bonus)

    @property
    def base_damage(self):
        return self.base_damage

    @base_damage.setter
    def base_damage(self, base_damage):
        if base_damage < 0:
            self.base_damage = 0
        elif base_damage > self.max_damage:
            self.base_damage = self.max_damage
        else:
            self.base_damage = base_damage

    @property
    def max_damage(self):
        return self.max_damage

    @max_damage.setter
    def max_damage(self, max_damage):
        if max_damage < 0:
            self.max_damage = 0
        elif max_damage < self.base_damage:
            self.max_damage = self.base_damage
        else:
            self.max_damage = max_damage

    @property
    def crit_chance(self):
        return self.crit_chance

    @crit_chance.setter
    def crit_chance(self, crit_chance):
        if crit_chance < 0:
            self.crit_chance = 0
        elif crit_chance > 1:
            self.crit_chance = 1
        else:
            self.crit_chance = crit_chance

    @property
    def crit_bonus(self):
        return self.crit_bonus

    @crit_bonus.setter
    def crit_bonus(self, crit_bonus):
        self.crit_bonus = 0 if crit_bonus < 0 else crit_bonus

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, weight):
        self.weight = 0 if weight < 0 else weight

    def attack(self):
        """
        Generates amount of damage to do.

        Generates random number between base_damage and max_damage.
        If crit_chance > 0 and crit_chance greater than generated float then adds crit_bonus * attack
        """
        attack = randbelow(self.max_damage - 1) + self.base_damage
        if self.crit_chance and randbelow(1) < self.crit_chance:
            attack += attack * self.crit_bonus
        return attack
