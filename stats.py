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
        Regenerates health.

        Keyword arguments:
            amount -- amount to regenerate

        Accepts either none or an int.
        If none calculates amount to regen using max * regen_rate.
        Adds that amount to current health if not already maxed.
        """
        if not amount:
            amount = int(self.max * self.regen_rate)
        else:
            if type(amount) != int:
                amount = int(amount)
        self.current += amount
        if self.current > self.max:
            amount = self.max - self.current
            self.current = self.max
        return amount


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


class LevelStat:
    def __init__(self, level=1, xp=0, max_xp=100, xp_rate=.2):
        self.level = level
        self.max_xp = max_xp
        self.xp_rate = xp_rate
        self.xp = xp

    @property
    def level(self):
        return self.level

    @level.setter
    def level(self, level):
        self.level = 0 if level < 0 else level

    @property
    def max_xp(self):
        return self.max_xp

    @max_xp.setter
    def max_xp(self, max_xp):
        if max_xp < 0:
            self.max_xp = 0
        elif max_xp <= self.xp:
            self.max_xp = self.xp
            self.level_up()
        else:
            self.max_xp = max_xp

    def level_up(self):
        """
        Levels up.

        Returns whether or not the level up happened.
        """
        if self.xp >= self.max_xp:
            self.level += 1
            self.xp -= self.max_xp
            self.max_xp += self.max_xp * self.xp_rate
            return True
        return False

    @property
    def xp(self):
        return self.xp

    @xp.setter
    def xp(self, xp):
        self.xp = 0 if xp < 0 else xp
        if self.xp >= self.max_xp:
            self.level_up()

    @property
    def xp_rate(self):
        return self.xp_rate

    @xp_rate.setter
    def xp_rate(self, xp_rate):
        self.xp_rate = 0 if xp_rate < 0 else xp_rate

    def __str__(self):
        return 'Level: {}, {}/{}'.format(self.level, self.xp, self.max_xp)

    def __repr__(self):
        return '{}(level={}, xp={}, max_xp={}, xp_rate={})'.format(self.__class__.__name__, self.level, self.xp,
                                                                   self.max_xp, self.xp_rate)
