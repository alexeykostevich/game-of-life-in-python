import unittest
from game_of_life import Cell


class CellTestCase(unittest.TestCase):
    def test_str(self):
        cell = Cell()

        self.assertEqual(str(cell), '*')

    def test_likely(self):
        cells = [Cell.likely() for _ in range(10)]

        cells_count = sum(isinstance(cell, Cell) for cell in cells)
        none_count = sum(cell is None for cell in cells)

        self.assertTrue(0 < cells_count < 10)
        self.assertTrue(0 < none_count < 10)


if __name__ == '__main__':
    unittest.main()
