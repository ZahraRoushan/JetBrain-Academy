"""
*** Stage 3/6: Where to next? ***

Description

Once the board is set up, let's see where our knight can move.

The knight moves in an L-shape,
so it has to move 2 squares horizontally and 1 square vertically, or 2 squares vertically and 1 square horizontally.

In the second example, there are only 3 possible moves since the knight cannot leave the board.

------------
Objectives

In this stage, you should modify your program to do the following:

1- Check all 8 possible moving directions from the starting position.
2- If the move is possible, mark the landing position with the letter 'O'.
3- If the move is not possible, no action is required.

Don't forget that column and row numbers, as well as the knight position and the 'O' letter for the landing position,
should be aligned to the right. For example, for a three-symbols long placeholder, the landing position should look like O.

------------
Example 1

Enter your board dimensions: > 6 5
Enter the knight's starting position: > 4 2

Here are the possible moves:
 ---------------------
5| __ __ __ __ __ __ |
4| __ __  O __  O __ |
3| __  O __ __ __  O |
2| __ __ __  X __ __ |
1| __  O __ __ __  O |
 ---------------------
    1  2  3  4  5  6


Example 2

Enter your board dimensions: > 3 4
Enter the knight's starting position: > 2 2

Here are the possible moves:
 ------------
4|  O __  O |
3| __ __ __ |
2| __  X __ |
1| __ __ __ |
 ------------
    1  2  3


Example 3

Enter your board dimensions: > 1 2
Enter the knight's starting position: > 1 2

Here are the possible moves:
 -----
2| X |
1| _ |
 -----
   1
"""


def check_input(column=5000, row=5000,
                input_massage='Enter your input!', error_massage='Invalid!'):
    while True:
        try:
            a, b = input(input_massage).split(' ')
            if 0 < int(a) <= column and 0 < int(b) <= row:
                break
            else:
                print(error_massage)
        except ValueError:
            print(error_massage)
    return int(a), int(b)


board_column, board_row = check_input(input_massage='Enter your board dimensions:',
                                      error_massage='Invalid dimensions!')


y, x = check_input(board_column, board_row,
                   input_massage="Enter the knight's starting position:",
                   error_massage='Invalid position!')

cell_size = len(str(board_row * board_column))
border_length = board_column * (cell_size + 1) + 3

# printing upper border
print((' ' * len(str(board_row))) + ('-' * border_length))

# make a matrix of the board
board = [['_' * cell_size for square in range(board_column)] for row in range(board_row)]
board[board_row - x][y - 1] = ' ' * (cell_size - 1) + 'X'

if board_column - y >= 2:  # two squares to the right
    if board_row - x >= 1:
        board[board_row - (x + 1)][y - 1 + 2] = ' ' * (cell_size - 1) + 'O'
    if x - 1 >= 1:
        board[board_row - x + 1][y - 1 + 2] = ' ' * (cell_size - 1) + 'O'

if y - 1 >= 2:  # two squares to the left
    if board_row - x >= 1:
        board[board_row - (x + 1)][y - 1 - 2] = ' ' * (cell_size - 1) + 'O'
    if x - 1 >= 1:
        board[board_row - x + 1][y - 1 - 2] = ' ' * (cell_size - 1) + 'O'

if board_row - x >= 2:  # two squares forward
    if board_column - y >= 1:
        board[board_row - (x + 2)][y - 1 + 1] = ' ' * (cell_size - 1) + 'O'
    if y - 1 >= 1:
        board[board_row - (x + 2)][y - 1 - 1] = ' ' * (cell_size - 1) + 'O'

if x - 1 >= 2: # two squares backward
    if board_column - y >= 1:
        board[board_row - x + 2][y - 1 + 1] = ' ' * (cell_size - 1) + 'O'
    if y - 1 >= 1:
        board[board_row - x + 2][y - 1 - 1] = ' ' * (cell_size - 1) + 'O'


# converting each row from list to a single string
for item in range(board_row):
    print(str(board_row - item) + '|', ' '.join(board[item]), '|')

# printing lower border
print((' ' * len(str(board_row))) + ('-' * border_length))

# printing board numbers
board_numbers = [' ' * (cell_size - 1) + str(num) for num in range(1, board_column + 1)]
board_numbers = ' '.join(board_numbers)
print(' ' * (len(str(board_row)) + 1), board_numbers, ' ' * len(str(board_row)))
