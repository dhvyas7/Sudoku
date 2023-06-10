from PySide6.QtWidgets import *
from PySide6.QtCore import *

import sys
import Logic.parent as parent

sudoku = parent.creator()
app = QApplication(sys.argv)

global selected_cell
selected_cell = QPushButton()
global is_selected
is_selected = False
cells = []


def window():
    win = QWidget()
    grid = QGridLayout()
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] != 0:
                cell = QPushButton(str(sudoku[i][j]))
                cell.setDisabled(True)
                cell.setStyleSheet("color: #000")
                cell.setFixedHeight(70)
                cells.append(cell)
                grid.addWidget(cell, i, j)
            else:
                cell = QPushButton("")
                cell.clicked.connect(lambda *args, arg=cell: select_box(arg))
                cell.setFixedHeight(70)
                cells.append(cell)
                grid.addWidget(cell, i, j)
    for i in range(9):
        num_button = QPushButton(str(i + 1))
        num_button.clicked.connect(lambda *args, num=i: choose_num(num))
        num_button.setMinimumHeight(20)
        grid.addWidget(num_button)

    for i in range(7):
        cell = QPushButton("")
        cell.setDisabled(True)
        cell.setStyleSheet("background-color: #f2f2f2; border: default")
        grid.addWidget(cell)

    check_button = QPushButton("Check")
    check_button.clicked.connect(check)
    grid.addWidget(check_button)

    reset_button = QPushButton("Reset")
    reset_button.clicked.connect(reset)
    grid.addWidget(reset_button)

    win.setLayout(grid)
    win.setWindowTitle("Sudoku")
    win.setGeometry(50, 50, 200, 200)
    win.show()
    sys.exit(app.exec_())


def select_box(cell):
    global selected_cell
    temp_cell = selected_cell
    global is_selected
    temp_bool = is_selected

    if temp_cell != cell and not(temp_bool):
        selected_cell = cell
        is_selected = True
        cell.setStyleSheet(
            "border: 2px solid blue; border-style:groove;")
    elif temp_cell != cell and temp_bool:
        selected_cell.setStyleSheet("")
        selected_cell = cell
        cell.setStyleSheet(
            "border: 2px solid blue; border-style:groove;")
    else:
        selected_cell = 0
        is_selected = False
        cell.setStyleSheet("")


def choose_num(num):
    global selected_cell
    temp_cell = selected_cell
    temp_cell.setText(str(num + 1))


def check():
    cell_vals = []
    for i in range(9):
        cell_vals.append([])
        for j in range(9):
            if cells[i * 9 + j].text() != '':
                cell_vals[i].append(int(cells[i * 9 + j].text()))
            else:
                cell_vals[i].append(0)
    val = parent.check(cell_vals)
    if val:
        print('Congratulations! You have won a free Snake Game')
        import snek
        snek.game()

    else:
        print('You have not solved the Sudoku :(')


def reset():
    for cell in cells:
        if cell.isEnabled():
            cell.setText("")
