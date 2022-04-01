"""
*** Stage 1/6: Setting up the board ***

Description

The knight's tour problem uses a chessboard and a knight.
Don't worry, you won't need to know the chess basics for this project, you only need to know
how a knight moves on the board.
A standard chess board is an 8x8 square on which the chess pieces are placed.
For this project, we will use a coordinate system (x,y) to label each square on the chessboard,
where (1,1) is the bottom left, and (8,8) is the top right.

The rules of the knight's tour are as follows:

The knight can start at any square.
The knight must visit every square by moving in the L-shape.
The knight can visit each square only once.
The knight can finish anywhere on the board. This is called an 'open' tour of the board.
You win if you visit every square on the board.
You lose if you fail to visit every square only once without revisiting it.

------------
Objectives
Let's get started by setting up the puzzle:

1- Ask the user for the knight's starting position.
2- If the user input contains non-integer numbers you should print Invalid dimensions!.
3- If the user input contains more than 2 numbers you should print Invalid dimensions!.
4- If the user input numbers out of bounds of the game field you should print Invalid dimensions!.
5- Display the 8x8 chessboard with the knight in this position. You should display a frame around the board
and mark the column and row numbers. You should use an underscore _ for an empty cell with a space in between them,
and an X for the knight's position.

------------
Example:

Enter the knight's starting position: > 1 3
 -------------------
8| _ _ _ _ _ _ _ _ |
7| _ _ _ _ _ _ _ _ |
6| _ _ _ _ _ _ _ _ |
5| _ _ _ _ _ _ _ _ |
4| _ _ _ _ _ _ _ _ |
3| X _ _ _ _ _ _ _ |
2| _ _ _ _ _ _ _ _ |
1| _ _ _ _ _ _ _ _ |
 -------------------
   1 2 3 4 5 6 7 8

"""

chess = [['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_']]

try:
    a, b = input("Enter the knight's starting position:").split(' ')
    if a.isdigit() and b.isdigit() and 0 < int(a) < 9 and 0 < int(b) < 9:
        a = int(a)
        b = int(b)
        chess[a][b] = 'X'
        print(' -------------------')
        for item in range(7, 0, -1):
            print(str(item + 1) + '|', chess[item], '|')
        print(' -------------------')
        print('   1 2 3 4 5 6 7 8 ')
    else:
        print('Invalid dimensions!')
except ValueError:
    print('Invalid dimensions!')
