from sparse_grid import SparseGrid
from random import randint


grid = SparseGrid.random(10, 10, lambda x, y: randint(0, 1))

print(grid)
