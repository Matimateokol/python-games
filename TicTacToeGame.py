from random import randrange

def setup_board():
    board = [[i + j*3 for i in range(1,4)] for j in range(3)]
    board[1][1] = "X"
    
    return board

def display_board(board):
    # Function takes an argument containing actual array's state
    # and displays it in console.
    for row in board:
        print(row)
    print()
    
def enter_move(board):
    # Function takes an argument representing the array's actual state
    # ask the player to make a move, 
    # checks input and updates the board according to player's decision.
    
    row = int(input("Enter the number of row (0-2): "))
    column = int(input("Enter the number of column (0-2): "))
    
    if (row, column) in make_list_of_free_fields(board):
        board[row][column] = "O"
        return True
    else:
        print("Invalid move. Try again.")
        return False

def make_list_of_free_fields(board):
    # Function search the board and make a list of all free fields; 
    # list consists of tuples and every tuple contains a pair of numbers what stands for row and column.
    free_fields = []
    for row in range(3):
        for column in range(3):
            if board[row][column] in range(1,10):
                free_fields.append((row, column))
    return free_fields

def victory_for(board, sign):
    # Fuction analyzes the board to check if the player ("O") or computer ("X") has won the game.
    winning_combinations = [
                            tuple(board[0][column] for column in range(3)),
                            tuple(board[1][column] for column in range(3)),
                            tuple(board[2][column] for column in range(3)),
                            tuple(board[row][0] for row in range(3)),
                            tuple(board[row][1] for row in range(3)),
                            tuple(board[row][2] for row in range(3)),
                            tuple(board[row][column] for row, column in zip(range(3), range(3))),
                            tuple(board[row][column] for row, column in zip(range(3), range(2,-1, -1)))
                            ]
                            
    if (sign, sign, sign) in winning_combinations:
        print("Won:", sign)
        return True
    else:
        return False
    
def draw_move(board):
    # Functions make a move for computer and updates the board.
    move = randrange(1,10)

    for ele in make_list_of_free_fields(board):
        if board[ele[0]][ele[1]] == int(move):
            board[ele[0]][ele[1]] = "X"
            return True

def play_new_game():
    board = setup_board()
    isPlayerTurn = True
    hasGameEnded = False
    
    while not hasGameEnded:
        display_board(board)

        # Checking if draw
        if make_list_of_free_fields(board) == []:
            hasGameEnded = True
            print("Draw")
            continue
        
        if isPlayerTurn:
            hasMoved = False
            while not hasMoved:
                hasMoved = enter_move(board)
            isPlayerTurn = False
            hasGameEnded = victory_for(board, "O")
            continue
        elif not isPlayerTurn:
            hasMoved = False
            while not hasMoved:
                hasMoved = draw_move(board)
            isPlayerTurn = True
            hasGameEnded = victory_for(board, "X")
            continue

play_new_game()
