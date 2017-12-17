import unittest
from life import ClosedUniverse


class ClosedUniverseTestCase(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            ClosedUniverse(0, 1)

        with self.assertRaises(ValueError):
            ClosedUniverse(1, 0)

        with self.assertRaises(ValueError):
            ClosedUniverse(-1, 1)

        with self.assertRaises(ValueError):
            ClosedUniverse(1, -1)

        self.assertIsInstance(ClosedUniverse(1, 1), ClosedUniverse)

    def test_width(self):
        universe = ClosedUniverse(2, 1)

        self.assertEqual(universe.width, 2)

    def test_height(self):
        universe = ClosedUniverse(1, 2)

        self.assertEqual(universe.height, 2)

    def test_empty(self):
        universe = ClosedUniverse.from_data([
            [1, 2],
            [3, None]
        ])

        empty_universe = universe.empty()

        self.assertEqual(empty_universe.width, universe.width)
        self.assertEqual(empty_universe.height, universe.height)

        all_empty = all(empty_universe[position] is None for position in empty_universe.through())

        self.assertTrue(all_empty)

    def test_through(self):
        universe = ClosedUniverse(2, 2)

        self.assertEqual(list(universe.through()), [(0, 0), (1, 0), (0, 1), (1, 1)])

    def test_neighbours_of(self):
        universe = ClosedUniverse.from_data([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        neighbours = universe.neighbours_of(0, 0)
        self.assertEqual(list(neighbours), [2, 5, 4])

        neighbours = universe.neighbours_of(2, 2)
        self.assertEqual(list(neighbours), [5, 6, 8])

        neighbours = universe.neighbours_of(1, 1)
        self.assertEqual(list(neighbours), [1, 2, 3, 6, 9, 8, 7, 4])

    def test_adjust_position(self):
        universe = ClosedUniverse(2, 2)

        with self.assertRaises(IndexError):
            universe.adjust_position(-1, 0)

        with self.assertRaises(IndexError):
            universe.adjust_position(2, 0)

        with self.assertRaises(IndexError):
            universe.adjust_position(0, -1)

        with self.assertRaises(IndexError):
            universe.adjust_position(0, 2)

        self.assertEqual(universe.adjust_position(0, 0), (0, 0))

    def test_is_position_in_range(self):
        universe = ClosedUniverse(2, 2)

        self.assertFalse(universe.is_position_in_range(-1, 0))
        self.assertFalse(universe.is_position_in_range(2, 0))
        self.assertFalse(universe.is_position_in_range(0, -1))
        self.assertFalse(universe.is_position_in_range(0, 2))
        self.assertTrue(universe.is_position_in_range(0, 0))

    def test_get_item(self):
        universe = ClosedUniverse.from_data([
            [1, 3],
            [2, None]
        ])

        self.assertEqual(universe[0, 0], 1)
        self.assertEqual(universe[1, 1], None)

        with self.assertRaises(IndexError):
            universe[-1, 0]

        with self.assertRaises(IndexError):
            universe[2, 0]

        with self.assertRaises(IndexError):
            universe[0, -1]

        with self.assertRaises(IndexError):
            universe[0, 2]

    def test_set_item(self):
        universe = ClosedUniverse(2, 2)

        universe[0, 0] = 1
        self.assertEqual(universe[0, 0], 1)

        universe[1, 1] = 2
        self.assertEqual(universe[1, 1], 2)

        with self.assertRaises(IndexError):
            universe[-1, 0] = 3

        with self.assertRaises(IndexError):
            universe[2, 0] = 4

        with self.assertRaises(IndexError):
            universe[0, -1] = 5

        with self.assertRaises(IndexError):
            universe[0, 2] = 6

    def test_str(self):
        universe = ClosedUniverse.from_data([
            [None, 3],
            [2, None]
        ])

        self.assertMultiLineEqual(str(universe), '  3\n2  ')

    def test_eq(self):
        left = ClosedUniverse.from_data([
            [1, 3],
            [2, None]
        ])

        right = ClosedUniverse.from_data([
            [1, 3],
            [2, None]
        ])

        self.assertEqual(left, right)

        left = ClosedUniverse.from_data([
            [1, 3],
            [2, None]
        ])

        right = ClosedUniverse.from_data([
            [1, 3],
            [2, 4]
        ])

        self.assertNotEqual(left, right)

    def test_from_data(self):
        universe = ClosedUniverse.from_data([
            [0, 1],
            [2, 3, 4]
        ])

        self.assertEqual(universe.width, 2)
        self.assertEqual(universe.height, 2)

        self.assertIsNone(universe[0, 0])
        self.assertEqual(universe[1, 0], 1)
        self.assertEqual(universe[0, 1], 2)
        self.assertEqual(universe[1, 1], 3)

        universe = ClosedUniverse.from_data([
            [0, '*'],
            [2, '*', '*']
        ], lambda cell: cell == '*')

        self.assertEqual(universe.width, 2)
        self.assertEqual(universe.height, 2)

        self.assertIsNone(universe[0, 0])
        self.assertEqual(universe[1, 0], '*')
        self.assertIsNone(universe[0, 1])
        self.assertEqual(universe[1, 1], '*')

        with self.assertRaises(ValueError):
            universe = ClosedUniverse.from_data([])

        with self.assertRaises(ValueError):
            universe = ClosedUniverse.from_data([[]])

    def test_random(self):
        universe = ClosedUniverse.random(2, 2, lambda: 1)

        self.assertEqual(universe.width, 2)
        self.assertEqual(universe.height, 2)
        self.assertEqual(universe[0, 0], 1)
        self.assertEqual(universe[1, 0], 1)
        self.assertEqual(universe[0, 1], 1)
        self.assertEqual(universe[1, 1], 1)


if __name__ == '__main__':
    unittest.main()
