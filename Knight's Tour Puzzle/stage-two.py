"""
*** Stage 1/6: Setting up the board ***

Description

The traditional version of the puzzle uses a standard chessboard, but you can use a board of any size.
You can try smaller boards like 5×5, rectangular boards like 4×8, or even non-rectangular boards with some squares missing!
Here, we will only focus on rectangular boards.
Note that the board is guaranteed to have a solution if the smallest dimension is at least 5.
Smaller boards may not have a solution.

------------
Objectives

In this stage, you should modify your program to do the following:

1- Ask the user for the board's dimensions using X for columns and Y for rows.
2- If the board's dimensions contain non-integer numbers print Invalid dimensions!.
3- If the board's dimensions contain more than 2 numbers print Invalid dimensions!.
4- If the board's dimensions contain negative numbers print Invalid dimensions!.
5- If invalid dimensions were provided by the user, ask them for valid dimensions again after outputting Invalid dimensions!
6- Once the starting position is determined, check whether it is valid as in the previous stage.
7- If not, you should show the Invalid position! error message and then prompt the user for another starting position.
8- Draw the board.

Use an underscore symbol _ to mark empty board squares; the number of underscore symbols for each empty square should be
chosen according to the total number of cells: there should be as many underscores for each cell as there are digits in
the total number of cells. For example, a 10 × 10 board has 100 spaces, so your placeholder should be ___ for an empty cell.
If your board dimension is 6 x 5, your placeholder will be __. This will be used in later stages.

Make sure that the column numbers are exactly under the placeholders for the given column.
Also, make sure your column, row numbers, and the knight position are aligned to the right:
for example, the knight positions should be marked as _X or __X (instead of X_ or _X_),
depending on the number of underscores for each square.

The border's length also depends on the size of the field.
Use the following formula to calculate the length of the required border: column_n * (cell_size + 1) + 3,
where column_n is the number of columns, and cell_size is the length of a placeholder for one cell.

------------
Example 1

Enter your board dimensions: > 6 5
Enter the knight's starting position: > 4 2
 ---------------------
5| __ __ __ __ __ __ |
4| __ __ __ __ __ __ |
3| __ __ __ __ __ __ |
2| __ __ __  X __ __ |
1| __ __ __ __ __ __ |
 ---------------------
    1  2  3  4  5  6


Example 2

Enter your board dimensions: > 4 4
Enter the knight's starting position: > 8 8
Invalid position!
Enter the knight's starting position: > -1 2
Invalid position!
Enter the knight's starting position: > 2 2
 ---------------
4| __ __ __ __ |
3| __ __ __ __ |
2| __  X __ __ |
1| __ __ __ __ |
 ---------------
    1  2  3  4


Example 3

Enter your board dimensions: > 10 10
Enter the knight's starting position: > 5 5
  -------------------------------------------
10| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 9| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 8| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 7| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 6| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 5| ___ ___ ___ ___   X ___ ___ ___ ___ ___ |
 4| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 3| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 2| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 1| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
  -------------------------------------------
      1   2   3   4   5   6   7   8   9  10
"""

def check_dimension():
    while True:
            try:
                column, row = input("Enter your board dimensions:").split(' ')
                if row.isdigit() and column.isdigit() and 0 < int(row) and 0 < int(column):
                    break
                else:
                    print('Invalid dimensions!')
            except ValueError:
                print('Invalid dimensions!')
    return int(column), int(row)


def check_position(column, row):
    while True:
        try:
            a, b = input("Enter the knight's starting position:").split(' ')
            if a.isdigit() and b.isdigit() and 0 < int(a) <= column and 0 < int(b) <= row:
                break
            else:
                print('Invalid position!')
        except ValueError:
            print('Invalid position!')
    return int(a), int(b)


board_column, board_row = check_dimension()
y, x = check_position(board_column, board_row)
cell_size = len(str(board_row * board_column))
border_length = board_column * (cell_size + 1) + 3

# printing upper border
print((' ' * len(str(board_row))) + ('-' * border_length))

# make a matrix of the board
board = [[] for row in range(board_row)]
for idx, row in enumerate(board):
    for column in range(1, board_column + 1):
        if idx + 1 == x and column == y:
            row.append(' ' * (cell_size - 1) + 'X')
        else:
            row.append('_' * cell_size)

for item in range(board_row, 0, -1):
    print(str(item) + '|', ' '.join(board[item - 1]), '|')

print((' ' * len(str(board_row))) + ('-' * border_length))

board_numbers = [' ' * (cell_size - 1) + str(num) for num in range(1, board_column + 1)]
board_numbers = ' '.join(board_numbers)
print(' ' * (len(str(board_row)) + 1), board_numbers, ' ' * len(str(board_row)))
