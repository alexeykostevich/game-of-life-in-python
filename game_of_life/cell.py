import random


class Cell(object):
    def __str__(self) -> str:
        return '*'

    @classmethod
    def likely(cls) -> 'Cell':
        return random.choice([cls(), None])
