# PROJETO: Tic-Tac-Toe

from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print(
            f"+-------+-------+-------+\n|       |       |       |\n|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |\n|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board acording to the user's decision.
    move = int(input("Enter your move: "))

    # while move in board is True:
    #     move = int(input("Enter your move: "))

    if move > 0 and move < 10:

        # if move in board:

        if move <= 3:
            board[0][board[0].index(move)] = 'O'
            # print(board.index(move))
        elif move <= 6:
            board[1][board[1].index(move)] = 'O'
            # board[1].insert(move, 'O')
        elif move <= 9:
            board[2][board[2].index(move)] = 'O'
            # board[2].insert(move, 'O')


def make_list_of_free_field(board):
    # The function browses the board and buils a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    free_fields = []
    free_tuple = ()

    # for row in range(3):
    #     for column in range(3):
    #         if board[row][column] not in 'O' and board[row][column]  'X':

    # for row in range(len(board)):
    #     for column in range(len(board)):
    #         if board[column][row] != 'O':
    #             print(board[column][row])
    #
    #         if board[column][row] != 'X':
    #             print(board[column][row])

    for row in range(len(board)):
        for column in range(row):
            if 'O' in board[row][column] or 'X' in board[row][column]:
            print(board[row])



    print(free_fields)
        # free_tuple = tuple(free_tuple)
        # if 'O' in i or 'X' in i
        # print(i)
        # for j in i:
        #     if 'O' not in j and 'X' not in j:
        #         free_fields = tuple(j)
    # else:
    #     continue

    return free_fields


# def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #first_column = [0, 0, 0]
    #second_column = [1, 1, 1]
    #third_column = [2, 2, 2]

    #for columm in board:


    # def draw_move(board):
    # The function draws the computer's move and updates the board
    # computer_move = randrange(1, 9)
    # board[]


board = [[0 for i in range(3)] for j in range(3)]

numbers = 1

for row in range(len(board)):
    for column in range(len(board)):
        board[row][column] = numbers
        numbers += 1

board[1][1] = "X"

display_board(board)
enter_move(board)
display_board(board)
print(make_list_of_free_field(board))
# print(enter_move(board))
# print(board)
