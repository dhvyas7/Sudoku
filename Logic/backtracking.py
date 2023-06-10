import random


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.value = 0


def check_valid(grid, row, col, value):
    # Calls all Check Functions
    return check_row(grid, row, col, value) and check_col(grid, row, col, value) and check_box(grid, row, col, value)


def check_row(grid, row, col, value):
    # Checks if the number is valid in the row
    row_vals = []
    for i in range(len(grid[row])):
        if i != col:
            row_vals.append(grid[row][i].value)
    return value not in row_vals


def check_col(grid, row, col, value):
    # Checks if the number is valid in the column
    column = []
    for i in range(len(grid)):
        if i != row:
            column.append(grid[i][col].value)
    return value not in column


def check_box(grid, row, col, value):
    # Checks if the number is valid in the box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    box = []
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if i != row and j != col:
                box.append(grid[i][j].value)
    return value not in box


def main():
    grid = [[Cell(row, col) for col in range(9)] for row in range(9)]
    cell_pos = 0
    while cell_pos < 81:
        row = cell_pos // 9
        col = cell_pos % 9
        cell = grid[row][col]

        if len(cell.values) == 0:
            cell.values = list(range(1, 10))
            cell_pos -= 1
            continue
        while True:
            cell.value = random.choice(cell.values)
            valid = check_valid(grid, cell.row, cell.col, cell.value)
            if valid:
                cell_pos += 1
                break
            else:
                cell.values.remove(cell.value)
                cell.value = 0
                if len(cell.values) == 0:
                    cell.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    prev_cell_pos = cell_pos - 1
                    prev_cell_row = prev_cell_pos // 9
                    prev_cell_col = prev_cell_pos % 9
                    prev_cell = grid[prev_cell_row][prev_cell_col]

                    prev_cell.values.remove(prev_cell.value)

                    cell_pos -= 1
                    break

    return grid


main()
