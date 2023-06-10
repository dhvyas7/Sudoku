import random
import snek


class Sudoku:
    difficulties = {"beginner": 50, "intermediate": 60, "expert": 70, }

    def make_grid(self):
        # Todo make the grid using backtracking
        pass

    def remove_nums(self, grid, difficulty):
        num_remove = Sudoku.difficulties[difficulty]
        while num_remove > 0:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
            if grid[r][c] != 0:
                grid[r][c] = 0
                num_remove -= 1
        return grid


test_grid = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
             [9, 6, 5, 3, 2, 7, 1, 4, 8],
             [3, 4, 1, 6, 8, 9, 7, 5, 2],
             [5, 9, 3, 4, 6, 8, 2, 7, 1],
             [4, 7, 2, 5, 1, 3, 6, 8, 9],
             [6, 1, 8, 9, 7, 2, 4, 3, 5],
             [7, 8, 6, 2, 3, 5, 9, 1, 4],
             [1, 5, 4, 7, 9, 6, 8, 2, 3],
             [2, 3, 9, 8, 4, 1, 5, 6, 7]]

sudoku_handler = Sudoku()
sudoku_q = sudoku_handler.remove_nums(test_grid, "expert")
