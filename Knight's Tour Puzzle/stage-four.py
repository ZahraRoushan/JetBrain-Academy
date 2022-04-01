"""
*** Stage 4/6: Looking ahead ***

Description

It is time to find a winning strategy. At each point, the player may have different move options.
We could check every route combination, but it would take a long-long time.
With a computer program, we could use brute force to check every possible route until we find a solution.
However, this is inefficient and could take a while even for a computer. So what is the best way to crack this puzzle?
Warnsdorff's rule is here to help us.

Warnsdorff's rule is a strategy that helps choose the best move based on the knight's position and the board status.
To apply it, we need to do the following:

1- Check if each of the eight knight's moves is possible;
2- Check how many moves are possible from that landing position.
------------
Objectives

In this stage, you should modify your program to do the following:

1- From the starting position, check all eight possible moving directions.
2- If the move is possible, mark the square with a number that indicates how many distinct moves are possible from that square.
3- If the move is not possible, no action is required.

------------
Example 1

Enter your board dimensions: > 6 5
Enter the knight's starting position: > 4 2

Here are the possible moves:
 ---------------------
5| __ __ __ __ __ __ |
4| __ __  5 __  3 __ |
3| __  5 __ __ __  3 |
2| __ __ __  X __ __ |
1| __  2 __ __ __  1 |
 ---------------------
    1  2  3  4  5  6


Example 2

Enter your board dimensions: > 3 4
Enter the knight's starting position: > 2 2

Here are the possible moves:
 ------------
4|  1 __  1 |
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


def check_moves(a, b, board_height=board_column, board_length=board_row):
    count = 0
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
             [1, 2], [-1, 2], [1, -2], [-1, -2]]
    for move in moves:
        if 0 <= a + move[0] <= board_length - 1 and 0 <= b + move[1] <= board_height - 1:
            count += 1
    return count - 1


if board_column - y >= 2:  # two squares to the right
    if board_row - x >= 1:
        board[board_row - (x + 1)][y - 1 + 2] = ' ' * (cell_size - 1) + str(check_moves(board_row - (x + 1), y - 1 + 2))
    if x - 1 >= 1:
        board[board_row - x + 1][y - 1 + 2] = ' ' * (cell_size - 1) + str(check_moves(board_row - x + 1, y - 1 + 2))

if y - 1 >= 2:  # two squares to the left
    if board_row - x >= 1:
        board[board_row - (x + 1)][y - 1 - 2] = ' ' * (cell_size - 1) + str(check_moves(board_row - (x + 1), y - 1 - 2))
    if x - 1 >= 1:
        board[board_row - x + 1][y - 1 - 2] = ' ' * (cell_size - 1) + str(check_moves(board_row - x + 1, y - 1 - 2))

if board_row - x >= 2:  # two squares forward
    if board_column - y >= 1:
        board[board_row - (x + 2)][y - 1 + 1] = ' ' * (cell_size - 1) + str(check_moves(board_row - (x + 2), y - 1 + 1))
    if y - 1 >= 1:
        board[board_row - (x + 2)][y - 1 - 1] = ' ' * (cell_size - 1) + str(check_moves(board_row - (x + 2), y - 1 - 1))

if x - 1 >= 2:  # two squares backward
    if board_column - y >= 1:
        board[board_row - x + 2][y - 1 + 1] = ' ' * (cell_size - 1) + str(check_moves(board_row - x + 2, y - 1 + 1))
    if y - 1 >= 1:
        board[board_row - x + 2][y - 1 - 1] = ' ' * (cell_size - 1) + str(check_moves(board_row - x + 2, y - 1 - 1))


# converting each row from list to a single string
for item in range(board_row):
    print(str(board_row - item) + '|', ' '.join(board[item]), '|')

# printing lower border
print((' ' * len(str(board_row))) + ('-' * border_length))

# printing board numbers
board_numbers = [' ' * (cell_size - 1) + str(num) for num in range(1, board_column + 1)]
board_numbers = ' '.join(board_numbers)
print(' ' * (len(str(board_row)) + 1), board_numbers, ' ' * len(str(board_row)))
