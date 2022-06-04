"""
*** Stage 5/6: How far will your knight go ***

Description

Try and beat this puzzle! Your program should now allow multiple moves and mark the squares you have already visited.

The task is quite hard, and you may want to use Warnsdorff's rule to complete it.
Using the rule alone doesn't guarantee that you will win, so you can dismiss it if you prefer.
Bear in mind that not every board may have a solution!

------------
Objectives
In this stage, you should modify your program to do the following:

1. Set up a board.
2. Display the board status and the number of possible moves using Warnsdorff's rule.
3. Prompt the player for the knight's move.
4. Check whether the move is valid. If not, ask the player for another move.
5. Move the knight and mark the position with an 'X'. Mark the visited squares with an '*'.
6. Repeat the above step until there are no more possible moves.
7. If the player visits every square without repetition, congratulate them on their victory!
8. If the player loses, print the number of moves they made.

Please, try to organize your code well, split it into functions and methods, and make them reusable:
the difficulty of the next stage greatly depends on this.
Its implementation will involve the feature of solving the puzzle automatically.
This is not an easy task if your code isn't split into functions.

------------
Examples
The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the input.

Example 1

Enter your board dimensions: > 4 4
Enter the knight's starting position: > 2 2
 ---------------
4|  1 __  2 __ |
3| __ __ __  2 |
2| __  X __ __ |
1| __ __ __  1 |
 ---------------
    1  2  3  4

Enter your next move: > 2 2
Invalid move! Enter your next move: > 4 1
 ---------------
4| __ __ __ __ |
3| __ __  3 __ |
2| __  * __ __ |
1| __ __ __  X |
 ---------------
    1  2  3  4

Enter your next move: > 3 3
 ---------------
4|  0 __ __ __ |
3| __ __  X __ |
2|  2  * __ __ |
1| __  2 __  * |
 ---------------
    1  2  3  4

Enter your next move: > 1 4
 ---------------
4|  X __ __ __ |
3| __ __  * __ |
2| __  * __ __ |
1| __ __ __  * |
 ---------------
    1  2  3  4

No more possible moves!
Your knight visited 4 squares!
Example 2

Enter your board dimensions: > 5 4
Enter the knight's starting position: > 1 4
 ------------------
4|  X __ __ __ __ |
3| __ __  5 __ __ |
2| __  3 __ __ __ |
1| __ __ __ __ __ |
 ------------------
    1  2  3  4  5

Enter your next move: > 2 2
 ------------------
4|  * __  3 __ __ |
3| __ __ __  3 __ |
2| __  X __ __ __ |
1| __ __ __  2 __ |
 ------------------
    1  2  3  4  5

Enter your next move: > 4 1
 ------------------
4|  * __ __ __ __ |
3| __ __  4 __  2 |
2| __  * __ __ __ |
1| __ __ __  X __ |
 ------------------
    1  2  3  4  5

...

Enter your next move: > 3 1
 ------------------
4|  * __  *  *  * |
3|  *  *  *  *  * |
2|  1  *  *  *  * |
1|  *  *  X  *  * |
 ------------------
    1  2  3  4  5

Enter your next move: > 1 2
 ------------------
4|  *  0  *  *  * |
3|  *  *  *  *  * |
2|  X  *  *  *  * |
1|  *  *  *  *  * |
 ------------------
    1  2  3  4  5

Enter your next move: > 2 4
 ------------------
4|  *  X  *  *  * |
3|  *  *  *  *  * |
2|  *  *  *  *  * |
1|  *  *  *  *  * |
 ------------------
    1  2  3  4  5

What a great tour! Congratulations!

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

# make a matrix of the board
board = [['_' * cell_size for square in range(board_column)] for row in range(board_row)]
board[board_row - x][y - 1] = ' ' * (cell_size - 1) + 'X'


def count_possible_moves(a, b, board_height=board_column, board_length=board_row):
    count = 0
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
             [1, 2], [-1, 2], [1, -2], [-1, -2]]
    for move in moves:
        if 0 <= a + move[0] <= board_length - 1 and 0 <= b + move[1] <= board_height - 1:
            if board[a + move[0]][b + move[1]][-1] != 'X':
                if board[a + move[0]][b + move[1]][-1] != '*':
                    count += 1
    return count


def show_possible_moves(a, b, board_height=board_column, board_length=board_row):
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
             [1, 2], [-1, 2], [1, -2], [-1, -2]]
    for move in moves:
        if 0 <= a + move[0] <= board_length - 1 and 0 <= b + move[1] <= board_height - 1:
            if board[a + move[0]][b + move[1]][-1] != 'X':
                if board[a + move[0]][b + move[1]][-1] != '*':
                    board[a + move[0]][b + move[1]] = ' ' * (cell_size - 1) + str(count_possible_moves(a + move[0], b + move[1]))
    return board


def draw_board(game_board):
    print((' ' * len(str(board_row))) + ('-' * border_length))  # printing upper border
    for item in range(board_row):  # converting each row from list to a single string
        print(str(board_row - item) + '|', ' '.join(game_board[item]), '|')

    print((' ' * len(str(board_row))) + ('-' * border_length))  # printing lower border

    # printing board numbers
    board_numbers = [' ' * (cell_size - 1) + str(num) for num in range(1, board_column + 1)]
    board_numbers = ' '.join(board_numbers)
    print(' ' * (len(str(board_row)) + 1), board_numbers, ' ' * len(str(board_row)))


board = show_possible_moves(board_row - x, y - 1)
draw_board(board)


def restore_board(a, b, game_board):
    for row in game_board:
        for idx, square in enumerate(row):
            if square[-1] != '*':
                row[idx] = '_' * cell_size
    game_board[board_row - a][b - 1] = ' ' * (cell_size - 1) + '*'
    current_square = [int(a), int(b)]
    return game_board, current_square


def next_move(game_board, current_square):
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
             [1, 2], [-1, 2], [1, -2], [-1, -2]]
    while True:
        try:
            b, a = input('Enter your next move:').split(' ')
            if [int(a) - current_square[0], int(b) - current_square[1]] in moves:
                if game_board[board_row - int(a)][int(b) - 1][-1] != '*':
                    game_board[board_row - int(a)][int(b) - 1] = ' ' * (cell_size - 1) + 'X'
                    game_board = show_possible_moves(board_row - int(a), int(b) - 1)
                    break
            else:
                print('Invalid move! Enter your next move:')
        except ValueError:
            print('Invalid move! Enter your next move:')
    return int(a), int(b), game_board


visits = 1
while True:
    board, current_move = restore_board(x, y, board)
    x, y, board = next_move(board, current_move)
    draw_board(board)
    visits += 1
    # print('counted possible moves:', count_possible_moves(board_row - x, y - 1))
    if count_possible_moves(board_row - x, y - 1) == 0:
        if visits == board_row * board_column:
            print('What a great tour! Congratulations!')
            break
        print('No more possible moves!')
        print(f'Your knight visited {visits} squares!')
        break
