"""
*** Stage 1/5: Initial setup ***

Description

In this project, you'll write a game called Tic-Tac-Toe that you can play against your computer.
The computer will have three levels of difficulty — easy, medium, and hard.

To begin with, let's write a program that knows how to work with coordinates and determine the state of the game.

The top-left cell will have the coordinates (1, 1) and the bottom-right cell will have the coordinates (3, 3), as shown in this table:

(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)

The program should ask the user to enter the coordinates of the cell where they want to make a move.

Keep in mind that the first coordinate goes from left to right, and the second coordinate goes from top to bottom.
Also, notice that coordinates start with 1 and can be 1, 2, or 3.
But what if the user attempts to enter invalid coordinates?
This could happen if they try to enter letters or symbols instead of numbers, or the coordinates of an already occupied cell.
Your program needs to prevent these things from happening by checking the user's input and catching possible exceptions.

---------------
Objectives
The program should work in the following way:

1- Ask the user to provide the initial state of the 3x3 table with the first input line.
This must include nine symbols that can be X, O or _ (the latter represents an empty cell).
2- Output the specified 3x3 table before the user makes a move.
3- Request that the user enters the coordinates of the move they wish to make.
4- The user then inputs two numbers representing the cell in which they wish to place their X or O.
The game always starts with X, so the user's move should be made with this symbol if there are an equal number of X's and O's in the table.
If the table contains an extra X, the move should be made with O.
5- Analyze the user input and show messages in the following situations:
• This cell is occupied! Choose another one! — if the cell is not empty;
• You should enter numbers! — if the user tries to enter letters or symbols instead of numbers;
• Coordinates should be from 1 to 3! — if the user attempts to enter coordinates outside of the table's range.
6- Display the table again with the user's most recent move included.
7- Output the state of the game.
The possible states are:

Game not finished — when no side has three in a row, but the table still has empty cells;
Draw — when no side has three in a row, and the table is complete;
X wins — when there are three X's in a row;
O wins — when there are three O's in a row.
If the user provides invalid coordinates, the program should repeat the request until numbers that represent an empty cell on the table are supplied. You should ensure that the program only outputs the table twice — before the move and after the user makes a legal move.

---------------
Example 1:

Enter the cells: > _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: > 3 1
This cell is occupied! Choose another one!
Enter the coordinates: > one
You should enter numbers!
Enter the coordinates: > one three
You should enter numbers!
Enter the coordinates: > 4 1
Coordinates should be from 1 to 3!
Enter the coordinates: > 1 1
---------
| X X X |
| O O   |
| O X   |
---------
X wins


Example 2:

Enter the cells: > XX_XOXOO_
---------
| X X   |
| X O X |
| O O   |
---------
Enter the coordinates: > 3 3
---------
| X X   |
| X O X |
| O O O |
---------
O wins


Example 3:

Enter the cells: > OX_XOOOXX
---------
| O X   |
| X O O |
| O X X |
---------
Enter the coordinates: > 1 3
---------
| O X X |
| X O O |
| O X X |
---------
Draw


Example 4:

Enter the cells: >  _XO_OX___
---------
|   X O |
|   O X |
|       |
---------
Enter the coordinates: > 3 1
---------
|   X O |
|   O X |
| X     |
---------
Game not finished
"""


def make_move(board, sign):
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
                board[int(row) - 1][int(column) - 1] = sign
                break
        except ValueError:
            print('You should enter numbers!')

    return board


def draw_table(board):
    print('---------')
    for row in board:
        print('|', ' '.join(row), '|')
    print('---------')


initial_state = list(input('Enter the cells:').replace('_', ' '))
if initial_state.count('X') > initial_state.count('O'):
    symbol = 'O'
    opponent = 'X'
else:
    symbol = 'X'
    opponent = 'O'

table = []
while bool(initial_state):
    table.append(initial_state[:3])
    initial_state = initial_state[3:]

draw_table(table)
condition = True
empty_cell = []
while condition:
    table = make_move(table, symbol)
    draw_table(table)
    if (table[0][0] == table[1][1] == table[2][2]) and table[0][0] != ' ':
        print(f'{table[0][0]} wins')
        condition = False
        break
    elif (table[0][2] == table[1][1] == table[2][0]) and table[0][2] != ' ':
        print(f'{table[0][2]} wins')
        condition = False
        break

    for idx in range(3):
        if (table[idx][0] == table[idx][1] == table[idx][2]) and table[idx][0] != ' ':
            print(f'{table[idx][0]} wins')
            condition = False
            break

    for item in table:
        if item.count(symbol) == 3:
            print(f'{symbol} wins')
            condition = False
            break
        elif item.count(opponent) == 3:
            print(f'{opponent} wins')
            condition = False
            break
        elif ' ' in item:
            empty_cell.append(1)

    if any(empty_cell):
        print('Game not finished')
        continue
    else:
        print('Draw')
        condition = False
        break
