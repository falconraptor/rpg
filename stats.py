from numbers import Number


class RegenStat:
    def __str__(self):
        return 'Regen: {}/{}'.format(self.current, self.max)

    def __repr__(self):
        return '{}(current={}, max={}, regen_rate={})'.format(self.__class__.__name__, self.current, self.max,
                                                              self.regen_rate)

    def __init__(self, max=100, regen_rate=.01):
        self.max = max
        self.current = max
        self.regen_rate = regen_rate

    @property
    def current(self):
        return self.current

    @current.setter
    def current(self, current):
        if current < 0:
            self.current = 0
        elif current > self.max:
            self.current = self.max
        else:
            self.current = current

    @property
    def regen_rate(self):
        return self.regen_rate

    @regen_rate.setter
    def regen_rate(self, regen_rate):
        if regen_rate < 0:
            self.regen_rate = 0
        elif regen_rate > 1:
            self.regen_rate = 1
        else:
            self.regen_rate = regen_rate

    def regen(self, amount=None):
        """
        Regenerates a Stat.

        Keyword arguments:
            amount -- amount to regenerate

        Accepts either none or an Number (int, float).
        If none calculates amount to regen using max * regen_rate.
        Adds that amount to current health if not already maxed.

        Returns that amount.
        """
        if not amount:
            amount = self.max * self.regen_rate
        else:
            if not isinstance(amount, Number):
                amount = float(amount)
        self.current += amount
        if self.current > self.max:
            amount = self.current - self.max
            self.current = self.max
        return amount

    def __getitem__(self, item):
        if hasattr(self, item):
            self.__getattribute__(item)
        raise AttributeError('Attribute \'{}\' not defined'.format(item))


class ManaStat(RegenStat):
    def __init__(self, max=100, regen_rate=.01):
        super().__init__(max, regen_rate)

    def __str__(self):
        return 'Mana: {}/{}'.format(self.current, self.max)


class HealthStat(RegenStat):
    def __init__(self, max=100, regen_rate=.01):
        super().__init__(max, regen_rate)

    def __str__(self):
        return 'Health: {}/{}'.format(self.current, self.max)


class StaminaStat(RegenStat):
    def __init__(self, max=100, regen_rate=.01):
        super().__init__(max, regen_rate)

    def __str__(self):
        return 'Stamina: {}/{}'.format(self.current, self.max)


class LevelStat(RegenStat):
    def __init__(self, level=1, xp=0, max_xp=100, xp_rate=.2):
        super().__init__(max=max_xp, regen_rate=xp_rate)
        self.level = level
        self.current = xp

    @property
    def level(self):
        return self.level

    @level.setter
    def level(self, level):
        self.level = 0 if level < 0 else level

    @property
    def max(self):
        return self.max

    @max.setter
    def max(self, max):
        if max < 0:
            self.max = 0
        elif max <= self.current:
            self.max = self.current
            self.level_up()
        else:
            self.max = max

    def level_up(self):
        """
        Levels up.

        Returns whether or not the level up happened.
        """
        if self.current >= self.max:
            self.level += 1
            self.current -= self.max
            self.max += self.max * self.regen_rate
            return True
        return False

    @property
    def current(self):
        return self.current

    @current.setter
    def current(self, current):
        self.current = 0 if current < 0 else current
        if self.current >= self.max:
            self.level_up()

    def __str__(self):
        return 'Level: {}, {}/{}'.format(self.level, self.current, self.max)

    def __repr__(self):
        return '{}(level={}, xp={}, max_xp={}, xp_rate={})'.format(self.__class__.__name__, self.level, self.current,
                                                                   self.max, self.regen_rate)
