import unittest
from life import BoundedWorld


class BoundedWorldTestCase(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            BoundedWorld(0, 1)

        with self.assertRaises(ValueError):
            BoundedWorld(1, 0)

        with self.assertRaises(ValueError):
            BoundedWorld(-1, 1)

        with self.assertRaises(ValueError):
            BoundedWorld(1, -1)

        self.assertIsInstance(BoundedWorld(1, 1), BoundedWorld)

    def test_width(self):
        world = BoundedWorld(2, 1)

        self.assertEqual(world.width, 2)

    def test_height(self):
        world = BoundedWorld(1, 2)

        self.assertEqual(world.height, 2)

    def test_get_positions(self):
        world = BoundedWorld(2, 2)

        self.assertEqual(list(world.get_positions()), [(0, 0), (1, 0), (0, 1), (1, 1)])

    def test_get_neighbours_positions_of(self):
        world = BoundedWorld.from_data(
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        )

        positions = world.get_neighbours_positions_of(0, 0)
        self.assertEqual(list(positions), [(1, 0), (1, 1), (0, 1)])

        positions = world.get_neighbours_positions_of(2, 2)
        self.assertEqual(list(positions), [(1, 1), (2, 1), (1, 2)])

        positions = world.get_neighbours_positions_of(1, 1)
        self.assertEqual(list(positions), [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)])

    def test_get_neighbours_of(self):
        world = BoundedWorld.from_data(
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        )

        neighbours = world.get_neighbours_of(0, 0)
        self.assertEqual(list(neighbours), [2, 5, 4])

        neighbours = world.get_neighbours_of(2, 2)
        self.assertEqual(list(neighbours), [5, 6, 8])

        neighbours = world.get_neighbours_of(1, 1)
        self.assertEqual(list(neighbours), [1, 2, 3, 6, 9, 8, 7, 4])

    def test_get_rows(self):
        world = BoundedWorld.from_data(
            [1, 2],
            [3, None]
        )

        rows = [list(row) for row in world.get_rows()]

        self.assertEqual(rows, [[1, 2], [3, None]])

    def test_adjust_position(self):
        world = BoundedWorld(2, 2)

        with self.assertRaises(IndexError):
            world.adjust_position(-1, 0)

        with self.assertRaises(IndexError):
            world.adjust_position(2, 0)

        with self.assertRaises(IndexError):
            world.adjust_position(0, -1)

        with self.assertRaises(IndexError):
            world.adjust_position(0, 2)

        self.assertEqual(world.adjust_position(0, 0), (0, 0))

    def test_is_position_in_range(self):
        world = BoundedWorld(2, 2)

        self.assertFalse(world.is_position_in_range(-1, 0))
        self.assertFalse(world.is_position_in_range(2, 0))
        self.assertFalse(world.is_position_in_range(0, -1))
        self.assertFalse(world.is_position_in_range(0, 2))
        self.assertTrue(world.is_position_in_range(0, 0))

    def test_get_item(self):
        world = BoundedWorld.from_data(
            [1, 3],
            [2, None]
        )

        self.assertEqual(world[0, 0], 1)
        self.assertEqual(world[1, 1], None)

        with self.assertRaises(IndexError):
            world[-1, 0]

        with self.assertRaises(IndexError):
            world[2, 0]

        with self.assertRaises(IndexError):
            world[0, -1]

        with self.assertRaises(IndexError):
            world[0, 2]

    def test_set_item(self):
        world = BoundedWorld(2, 2)

        world[0, 0] = 1
        self.assertEqual(world[0, 0], 1)

        world[1, 1] = 2
        self.assertEqual(world[1, 1], 2)

        with self.assertRaises(IndexError):
            world[-1, 0] = 3

        with self.assertRaises(IndexError):
            world[2, 0] = 4

        with self.assertRaises(IndexError):
            world[0, -1] = 5

        with self.assertRaises(IndexError):
            world[0, 2] = 6

    def test_str(self):
        world = BoundedWorld.from_data(
            [None, 3],
            [2, None]
        )

        self.assertMultiLineEqual(str(world), '  3\n2  ')

    def test_empty_from(self):
        world = BoundedWorld.from_data(
            [1, 2],
            [3, None, 5]
        )

        empty_world = BoundedWorld.empty_from(world)

        self.assertEqual(empty_world.width, world.width)
        self.assertEqual(empty_world.height, world.height)

        all_empty = all(empty_world[position] is None for position in empty_world.get_positions())

        self.assertTrue(all_empty)

    def test_from_data(self):
        world = BoundedWorld.from_data(
            [1, 2],
            [3, None, 5]
        )

        self.assertEqual(world.width, 2)
        self.assertEqual(world.height, 2)
        self.assertEqual(world[0, 0], 1)
        self.assertEqual(world[1, 0], 2)
        self.assertEqual(world[0, 1], 3)
        self.assertEqual(world[1, 1], None)

        with self.assertRaises(IndexError):
            world[2, 1]

    def test_random(self):
        world = BoundedWorld.random(2, 2, lambda: 1)

        self.assertEqual(world.width, 2)
        self.assertEqual(world.height, 2)
        self.assertEqual(world[0, 0], 1)
        self.assertEqual(world[1, 0], 1)
        self.assertEqual(world[0, 1], 1)
        self.assertEqual(world[1, 1], 1)


if __name__ == '__main__':
    unittest.main()
