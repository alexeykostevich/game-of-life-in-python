from grid import Grid
from random import randint


grid = Grid.random(10, 10, lambda x, y: randint(0, 1))

print(grid)
