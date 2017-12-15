import unittest
from life import WrappedUniverse


class WrappedUniverseTestCase(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            WrappedUniverse(0, 1)

        with self.assertRaises(ValueError):
            WrappedUniverse(1, 0)

        with self.assertRaises(ValueError):
            WrappedUniverse(-1, 1)

        with self.assertRaises(ValueError):
            WrappedUniverse(1, -1)

        self.assertIsInstance(WrappedUniverse(1, 1), WrappedUniverse)

    def test_width(self):
        universe = WrappedUniverse(2, 1)

        self.assertEqual(universe.width, 2)

    def test_height(self):
        universe = WrappedUniverse(1, 2)

        self.assertEqual(universe.height, 2)

    def test_empty(self):
        universe = WrappedUniverse.from_data([
            [1, 2],
            [3, None, 5]
        ])

        empty_universe = universe.empty()

        self.assertEqual(empty_universe.width, universe.width)
        self.assertEqual(empty_universe.height, universe.height)

        all_empty = all(empty_universe[position] is None for position in empty_universe.through())

        self.assertTrue(all_empty)

    def test_through(self):
        universe = WrappedUniverse(2, 2)

        self.assertEqual(list(universe.through()), [(0, 0), (1, 0), (0, 1), (1, 1)])

    def test_neighbours_of(self):
        universe = WrappedUniverse.from_data([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        neighbours = universe.neighbours_of(0, 0)
        self.assertEqual(list(neighbours), [9, 7, 8, 2, 5, 4, 6, 3])

        neighbours = universe.neighbours_of(2, 2)
        self.assertEqual(list(neighbours), [5, 6, 4, 7, 1, 3, 2, 8])

        neighbours = universe.neighbours_of(1, 1)
        self.assertEqual(list(neighbours), [1, 2, 3, 6, 9, 8, 7, 4])

    def test_adjust_position(self):
        universe = WrappedUniverse(2, 2)

        self.assertEqual(universe.adjust_position(-1, -1), (1, 1))
        self.assertEqual(universe.adjust_position(2, 2), (0, 0))
        self.assertEqual(universe.adjust_position(0, 0), (0, 0))

    def test_is_position_in_range(self):
        universe = WrappedUniverse(2, 2)

        self.assertTrue(universe.is_position_in_range(-1, 0))
        self.assertTrue(universe.is_position_in_range(2, 0))
        self.assertTrue(universe.is_position_in_range(0, -1))
        self.assertTrue(universe.is_position_in_range(0, 2))
        self.assertTrue(universe.is_position_in_range(0, 0))

    def test_get_item(self):
        universe = WrappedUniverse.from_data([
            [1, 3],
            [2, None]
        ])

        self.assertEqual(universe[0, 0], 1)
        self.assertEqual(universe[1, 1], None)
        self.assertEqual(universe[-1, 0], 3)
        self.assertEqual(universe[2, 0], 1)
        self.assertEqual(universe[0, -1], 2)
        self.assertEqual(universe[0, 2], 1)

    def test_set_item(self):
        universe = WrappedUniverse(2, 2)

        universe[0, 0] = 1
        self.assertEqual(universe[0, 0], 1)

        universe[1, 1] = 2
        self.assertEqual(universe[1, 1], 2)

        universe[-1, 0] = 3
        self.assertEqual(universe[1, 0], 3)

        universe[2, 0] = 4
        self.assertEqual(universe[0, 0], 4)

        universe[0, -1] = 5
        self.assertEqual(universe[0, 1], 5)

        universe[0, 2] = 6
        self.assertEqual(universe[0, 0], 6)

    def test_str(self):
        universe = WrappedUniverse.from_data([
            [None, 3],
            [2, None]
        ])

        self.assertMultiLineEqual(str(universe), '  3\n2  ')

    def test_eq(self):
        left = WrappedUniverse.from_data([
            [1, 3],
            [2, None]
        ])

        right = WrappedUniverse.from_data([
            [1, 3],
            [2, None]
        ])

        self.assertEqual(left, right)

        left = WrappedUniverse.from_data([
            [1, 3],
            [2, None]
        ])

        right = WrappedUniverse.from_data([
            [1, 3],
            [2, 4]
        ])

        self.assertNotEqual(left, right)

    def test_from_data(self):
        universe = WrappedUniverse.from_data([
            [0, 1],
            [2, 3, 4]
        ])

        self.assertEqual(universe.width, 2)
        self.assertEqual(universe.height, 2)

        self.assertIsNone(universe[0, 0])
        self.assertEqual(universe[1, 0], 1)
        self.assertEqual(universe[0, 1], 2)
        self.assertEqual(universe[1, 1], 3)

        universe = WrappedUniverse.from_data([
            [0, '*'],
            [2, '*', '*']
        ], lambda cell: cell == '*')

        self.assertEqual(universe.width, 2)
        self.assertEqual(universe.height, 2)

        self.assertIsNone(universe[0, 0])
        self.assertEqual(universe[1, 0], '*')
        self.assertIsNone(universe[0, 1])
        self.assertEqual(universe[1, 1], '*')

    def test_random(self):
        universe = WrappedUniverse.random(2, 2, lambda: 1)

        self.assertEqual(universe.width, 2)
        self.assertEqual(universe.height, 2)
        self.assertEqual(universe[0, 0], 1)
        self.assertEqual(universe[1, 0], 1)
        self.assertEqual(universe[0, 1], 1)
        self.assertEqual(universe[1, 1], 1)


if __name__ == '__main__':
    unittest.main()
