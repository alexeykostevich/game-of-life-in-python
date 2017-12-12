from random import random


class Cell(object):
    def __str__(self) -> str:
        return '*'

    @classmethod
    def likely(cls) -> 'Cell':
        return Cell() if random() > .5 else None
