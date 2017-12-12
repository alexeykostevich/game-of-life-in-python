import unittest
from game_of_life import Cell


class CellTestCase(unittest.TestCase):
    def test_str(self):
        cell = Cell()

        self.assertEqual(str(cell), '*')

    def test_likely(self):
        cell = Cell.likely()

        self.assertTrue(isinstance(cell, Cell) or cell is None)


if __name__ == '__main__':
    unittest.main()
