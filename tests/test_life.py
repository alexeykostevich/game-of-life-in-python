from typing import List
from unittest import TestCase
from life import ClosedUniverse, live, originate_from


def neibours(count: int) -> List[bool]:
    return [1] * count + [None] * (8 - count)


class LifeTestCase(TestCase):
    def test_live_cell_remains_dead(self):
        for alive in range(3):
            next_cell = live(None, neibours(alive), lambda: 1)
            self.assertIsNone(next_cell)

        for neiboirs_exist in range(4, 8):
            next_cell = live(None, neibours(alive), lambda: 1)
            self.assertIsNone(next_cell)

    def test_live_cell_survives(self):
        for alive in range(2, 3):
            next_cell = live(1, neibours(alive), lambda: 2)
            self.assertTrue(next_cell)

    def test_live_cell_dies(self):
        for alive in range(2):
            next_cell = live(1, neibours(alive), lambda: 1)
            self.assertIsNone(next_cell)

        for alive in range(4, 9):
            next_cell = live(1, neibours(alive), lambda: 1)
            self.assertIsNone(next_cell)

    def test_live_cell_regenerates(self):
        next_cell = live(None, neibours(3), lambda: 1)
        self.assertTrue(next_cell)

    def test_originate_from_loaf(self):
        original_universe = ClosedUniverse.from_data([
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 1, 0]
        ])

        generation = originate_from(original_universe, lambda: 1)
        actual_universe = next(generation)

        self.assertEqual(actual_universe, original_universe)

    def test_originate_from_block(self):
        original_universe = ClosedUniverse.from_data([
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ])

        generation = originate_from(original_universe, lambda: 1)
        actual_universe = next(generation)

        self.assertEqual(actual_universe, original_universe)

    def test_originate_from_blinker(self):
        original_universe = ClosedUniverse.from_data([
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ])

        expected_universe = ClosedUniverse.from_data([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ])

        generation = originate_from(original_universe, lambda: 1)
        actual_universe = next(generation)

        self.assertEqual(actual_universe, expected_universe)

    def test_originate_from_toad(self):
        original_universe = ClosedUniverse.from_data([
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [1, 1, 1, 0],
            [0, 0, 0, 0]
        ])

        expected_universe = ClosedUniverse.from_data([
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 0, 0]
        ])

        generation = originate_from(original_universe, lambda: 1)
        actual_universe = next(generation)

        self.assertEqual(actual_universe, expected_universe)


if __name__ == '__main__':
    unittest.main()
