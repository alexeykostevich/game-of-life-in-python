import unittest
from game_of_life.sparse_grid import SparseGrid


class SparseGridTestCase(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            SparseGrid(0, 1)

        with self.assertRaises(ValueError):
            SparseGrid(1, 0)

        with self.assertRaises(ValueError):
            SparseGrid(-1, 1)

        with self.assertRaises(ValueError):
            SparseGrid(1, -1)

        self.assertIsInstance(SparseGrid(1, 1), SparseGrid)

    def test_width(self):
        grid = SparseGrid(2, 1)

        self.assertEqual(grid.width, 2)

    def test_height(self):
        grid = SparseGrid(1, 2)

        self.assertEqual(grid.height, 2)

    def test_get_positions(self):
        grid = SparseGrid(2, 2)

        self.assertEqual(list(grid.get_positions()), [(0, 0), (1, 0), (0, 1), (1, 1)])

    def test_get_neighbours_positions_for(self):
        grid = SparseGrid.from_data(
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        )

        positions = grid.get_neighbours_positions_for(0, 0)
        self.assertEqual(list(positions), [(1, 0), (1, 1), (0, 1)])

        positions = grid.get_neighbours_positions_for(2, 2)
        self.assertEqual(list(positions), [(1, 1), (2, 1), (1, 2)])

        positions = grid.get_neighbours_positions_for(1, 1)
        self.assertEqual(list(positions), [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)])

    def test_get_neighbours_for(self):
        grid = SparseGrid.from_data(
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        )

        neighbours = grid.get_neighbours_for(0, 0)
        self.assertEqual(list(neighbours), [2, 5, 4])

        neighbours = grid.get_neighbours_for(2, 2)
        self.assertEqual(list(neighbours), [5, 6, 8])

        neighbours = grid.get_neighbours_for(1, 1)
        self.assertEqual(list(neighbours), [1, 2, 3, 6, 9, 8, 7, 4])

    def test_get_rows(self):
        grid = SparseGrid.from_data(
            [1, 2],
            [3, None]
        )

        rows = [list(row) for row in grid.get_rows()]

        self.assertEqual(rows, [[1, 2], [3, None]])

    def test_get_columns(self):
        grid = SparseGrid.from_data(
            [1, 3],
            [2, None]
        )

        columns = [list(column) for column in grid.get_columns()]

        self.assertEqual(columns, [[1, 2], [3, None]])

    def test_adjust_position(self):
        grid = SparseGrid(2, 2)

        with self.assertRaises(IndexError):
            grid.adjust_position(-1, 0)

        with self.assertRaises(IndexError):
            grid.adjust_position(2, 0)

        with self.assertRaises(IndexError):
            grid.adjust_position(0, -1)

        with self.assertRaises(IndexError):
            grid.adjust_position(0, 2)

        self.assertEqual(grid.adjust_position(1, 1), (1, 1))

    def test_is_position_in_range(self):
        grid = SparseGrid(2, 2)

        self.assertFalse(grid.is_position_in_range(-1, 0))
        self.assertFalse(grid.is_position_in_range(2, 0))
        self.assertFalse(grid.is_position_in_range(0, -1))
        self.assertFalse(grid.is_position_in_range(0, 2))
        self.assertTrue(grid.is_position_in_range(0, 0))
        self.assertTrue(grid.is_position_in_range(1, 1))

    def test_get_item(self):
        grid = SparseGrid.from_data(
            [1, 3],
            [2, None]
        )

        self.assertEqual(grid[0, 0], 1)
        self.assertEqual(grid[1, 1], None)

        with self.assertRaises(IndexError):
            grid[-1, 0]

        with self.assertRaises(IndexError):
            grid[2, 0]

        with self.assertRaises(IndexError):
            grid[0, -1]

        with self.assertRaises(IndexError):
            grid[0, 2]

    def test_set_item(self):
        grid = SparseGrid(2, 2)

        grid[0, 0] = 1
        self.assertEqual(grid[0, 0], 1)

        grid[1, 1] = 1
        self.assertEqual(grid[1, 1], 1)

        with self.assertRaises(IndexError):
            grid[-1, 0] = 1

        with self.assertRaises(IndexError):
            grid[2, 0] = 1

        with self.assertRaises(IndexError):
            grid[0, -1] = 1

        with self.assertRaises(IndexError):
            grid[0, 2] = 1

    def test_str(self):
        grid = SparseGrid.from_data(
            [None, 3],
            [2, None]
        )

        self.assertMultiLineEqual(str(grid), '  3\n2  ')

    def test_from_data(self):
        grid = SparseGrid.from_data(
            [1, 2],
            [3, None, 5]
        )

        self.assertEqual(grid[0, 0], 1)
        self.assertEqual(grid[1, 0], 2)
        self.assertEqual(grid[0, 1], 3)
        self.assertEqual(grid[1, 1], None)

        with self.assertRaises(IndexError):
            grid[2, 1]


if __name__ == '__main__':
    unittest.main()
