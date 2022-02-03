SudokuData = dict[tuple[int, int], int]

# Helper Methods

def puzzle_solved(puzzle: SudokuData) -> bool:
    return not any(v == 0 for _, v in puzzle.items())


def row_contains_value(puzzle: SudokuData, row: int, col: int, value: int) -> bool:
    return value in [v for k, v in puzzle.items() if k[0] != col and k[1] == row]


def col_contains_value(puzzle: SudokuData, row: int, col: int, value: int) -> bool:
    return value in [v for k, v in puzzle.items() if k[1] != row and k[0] == col]


def box_contains_value(puzzle: SudokuData, row: int, col: int, value: int) -> bool:
    bRow = (row // 3) * 3
    bRowRange = range(bRow, bRow + 3)
    bCol = (col // 3) * 3
    bColRange = range(bCol, bCol + 3)

    return value in [v for k, v in puzzle.items() if k[0] in bColRange and k[1] in bRowRange and k[0] != col and k[1] != row]


def row_complete(puzzle: SudokuData, row: int) -> bool:
    return {v for k, v in puzzle.items() if k[1] == row and v != 0}.__len__() == 9


def col_complete(puzzle: SudokuData, col: int) -> bool:
    return {v for k, v in puzzle.items() if k[0] == col and v != 0}.__len__() == 9


def box_complete(puzzle: SudokuData, row: int, col: int) -> bool:
    bRow = (row // 3) * 3
    bRowRange = range(bRow, bRow + 3)
    bCol = (col // 3) * 3
    bColRange = range(bCol, bCol + 3)

    return {v for k, v in puzzle.items() if k[0] in bColRange and k[1] in bRowRange and v != 0}.__len__() == 9

# Algorithms

def solve_recursive(puzzle: SudokuData, row: int, col: int) -> None:
    """Solve a sudoku puzzle recursively

    This algorithm will always find a solution, but can be slow given the number of squares which have been solved.
    """
    # print(f'Attempting to solve: {col, row}...')
    if puzzle_solved(puzzle): 
        # print('Puzzle complete!')
        return

    if row > 8:
        # print('Past number of rows in puzzle')
        return
    
    if puzzle[(col, row)] != 0:
        solve_recursive(puzzle, row + 1 if col == 8 else row, col + 1 if col < 8 else 0)
    else:
        for num in range(1, 10):
            if not row_contains_value(puzzle, row, col, num) and not col_contains_value(puzzle, row, col, num) and not box_contains_value(puzzle, row, col, num):
                puzzle[(col, row)] = num
                solve_recursive(puzzle, row + 1 if col == 8 else row, col + 1 if col < 8 else 0)
            
            if puzzle_solved(puzzle):
                return
            
        puzzle[(col, row)] = 0


# def solve_square(row: int, col: int) -> bool:
#     return False


# Classes

class Sudoku():
    """Class to represent a puzzle, which holds the solution and the current state
    """
    def __init__(self: 'Sudoku', puzzle: str):
        self.base: str = puzzle
        self.squares_visible: SudokuData = {(i % 9, i // 9):int(v) for i, v in enumerate(self.base)}
        self.squares_solved: SudokuData = {(i % 9, i // 9):int(v) for i, v in enumerate(self.base)}
        solve_recursive(self.squares_solved, 0, 0)

    def sudoku_solved(self: 'Sudoku') -> bool:
        return puzzle_solved(self.squares_solved)
    
    def sudoku_complete(self: 'Sudoku') -> bool:
        return puzzle_solved(self.squares_visible)
    
    def submit_number(self: 'Sudoku', row: int, col: int, value: int) -> bool:
        if value == self.squares_solved[(col, row)]:
            self.squares_visible[(col, row)] = value
            return True

        return False
