import unittest
from typing import List
from life import BoundedWorld, Cell, Life


def neibours(count: int) -> List[Cell]:
    return [Cell()] * count + [None] * (8 - count)


class BoundedWorldTestCase(unittest.TestCase):
    def test_next_cell_remains_dead(self):
        for alive in range(3):
            next_cell = Life.next_cell(None, neibours(alive))
            self.assertIsNone(next_cell)

        for neiboirs_exist in range(4, 8):
            next_cell = Life.next_cell(None, neibours(alive))
            self.assertIsNone(next_cell)

    def test_next_cell_remains_alive(self):
        cell = Cell()

        for alive in range(2, 3):
            next_cell = Life.next_cell(cell, neibours(alive))
            self.assertEqual(cell, next_cell)

    def test_next_cell_dies(self):
        cell = Cell()

        for alive in range(2):
            next_cell = Life.next_cell(cell, neibours(alive))
            self.assertIsNone(next_cell)

        for alive in range(4, 9):
            next_cell = Life.next_cell(cell, neibours(alive))
            self.assertIsNone(next_cell)

    def test_next_cell_regenerates(self):
        next_cell = Life.next_cell(None, neibours(3))
        self.assertIsInstance(next_cell, Cell)

    def test_originate_from_loaf(self):
        cell = Cell()

        original_world = BoundedWorld.from_data(
            [None, cell, cell, None],
            [cell, None, None, cell],
            [None, cell, None, cell],
            [None, None, cell, None]
        )

        next_world = next(Life.originate_from(original_world))

        self.assertEqual(next_world, original_world)

    def test_originate_from_block(self):
        cell = Cell()

        original_world = BoundedWorld.from_data(
            [None, None, None, None],
            [None, cell, cell, None],
            [None, cell, cell, None],
            [None, None, None, None]
        )

        next_world = next(Life.originate_from(original_world))

        self.assertEqual(next_world, original_world)

    def test_originate_from_blinker(self):
        cell = Cell()

        original_world = BoundedWorld.from_data(
            [None, cell, None],
            [None, cell, None],
            [None, cell, None]
        )

        expected_world = BoundedWorld.from_data(
            [None, None, None],
            [cell, cell, cell],
            [None, None, None]
        )

        next_world = next(Life.originate_from(original_world))

        self.assertEqual(str(next_world), str(expected_world))

    def test_originate_from_toad(self):
        cell = Cell()

        original_world = BoundedWorld.from_data(
            [None, None, None, None],
            [None, cell, cell, cell],
            [cell, cell, cell, None],
            [None, None, None, None]
        )

        expected_world = BoundedWorld.from_data(
            [None, None, cell, None],
            [cell, None, None, cell],
            [cell, None, None, cell],
            [None, cell, None, None]
        )

        next_world = next(Life.originate_from(original_world))

        self.assertEqual(str(next_world), str(expected_world))


if __name__ == '__main__':
    unittest.main()
