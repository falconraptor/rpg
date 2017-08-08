from effects import Effect
from stats import LevelStat


class Ability:
    def __init__(self, name, effects, level=None):
        self.name = name
        if not isinstance(effects, iter):
            effects = [effects]
        self.effects = [e for e in effects if isinstance(e, Effect)]
        self.level = level if level and isinstance(level, LevelStat) else LevelStat()
