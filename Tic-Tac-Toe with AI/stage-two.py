"""
*** Stage 2/5: Easy does it ***
Now it's time to make a working game, so let's create our first opponent! In this version of the program,
the user will be playing as X, and the computer will be playing as O at easy level. This will be our first small step towards creating the AI!
Let's design it so that at this level the computer makes random moves. This should be perfect for people who have never played the game before!

---------------
Objectives

In this stage, you should implement the following:

1- Display an empty table when the program starts.
2- The user plays first as X, and the program should ask the user to enter cell coordinates.
3- Next, the computer makes its move as O, and the players then move in turn until someone wins or the game results in a draw.
4- Print the final outcome at the very end of the game.

---------------
Example:

---------
|       |
|       |
|       |
---------
Enter the coordinates: > 2 2
---------
|       |
|   X   |
|       |
---------
Making move level "easy"
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: > 3 3
---------
| O     |
|   X   |
|     X |
---------
Making move level "easy"
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: > 3 1
---------
| O     |
| O X   |
| X   X |
---------
Making move level "easy"
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: > 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins

"""


from random import randint


def make_move(board):
    while True:
        try:
            row, column = input('Enter the coordinates:').split()
            if row.isalpha() and column.isalpha():
                print('You should enter numbers!')
            elif int(row) < 1 or int(row) > 3 or int(column) < 1 or int(column) > 3:
                print('Coordinates should be from 1 to 3!')
            elif board[int(row) - 1][int(column) - 1] != ' ':
                print('This cell is occupied! Choose another one!')
            else:
                board[int(row) - 1][int(column) - 1] = 'X'
                break
        except ValueError:
            print('You should enter numbers!')

    return board


def draw_table(board):
    print('---------')
    for row in board:
        print('|', ' '.join(row), '|')
    print('---------')


def check_condition(board):
    empty_cell = []
    game_end = False

    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != ' ':
        print(f'{board[0][0]} wins')
        game_end = True
    elif (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != ' ':
        print(f'{board[0][2]} wins')
        game_end = True

    for idx in range(3):
        if (board[idx][0] == board[idx][1] == board[idx][2]) and board[idx][0] != ' ':
            print(f'{board[idx][0]} wins')
            game_end = True

    for item in board:
        if item.count('X') == 3:
            print('X wins')
            game_end = True
        elif item.count('O') == 3:
            print('O wins')
            game_end = True
        elif ' ' in item:
            empty_cell.append(1)

    if not any(empty_cell):
        print('Draw')
        game_end = True

    return game_end


table = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
draw_table(table)
end = False

while not end:
    table = make_move(table)
    draw_table(table)
    end = check_condition(table)

    print('Making move level "easy"')
    while True:
        row = randint(0, 2)
        column = randint(0, 2)
        if table[row][column] == ' ':
            table[row][column] = 'O'
            break
    draw_table(table)
    end = check_condition(table)
