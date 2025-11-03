
#fuction creates the 3x3 board
def create_board():
    board = [] #board list
    for _ in range(3): #for loop '_' empty to ignore 'range' python function gives sequence of number 0 ->2
        row = ['', '', ''] # list making the first row of the board
        board.append(row)  #AH this here moves the next row in the board under each to get the 3x3
    return board # sends the completed 3x3 structure back for usage

board = create_board()

def pretty_board():
    for i, row in enumerate(board):
        row_display = [cell if cell != '' else '_' for cell in row]
        print(" | ".join(row_display))
        if i < 2:
            print("--+---+--")


def is_board_full():
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True

def check_winner(board, player):
    if board[row][0] == current_player and board[row][1] == current_player and board[row][2] == current_player:
        print("You Win!!!")
        return True

    if board[0][col] == current_player and board[1][col] == current_player and board[2][col] == current_player:
        print("You Win!!!")
        return True

    if row == col and board[0][0] == current_player and board[1][1] == current_player and board[2][
        2] == current_player:
        print("You Win!!!")
        return True

    if row + col == 2 and board[0][2] == current_player and board[1][1] == current_player and board[2][
        0] == current_player:
        print("You Win!!!")
        return True



# ask player for X & O
current_player = 'X'

print("Welcome to Tic Tac Toe!")

pretty_board()

while True:

    row = input(f"Player {current_player}, enter a row(1-3):")
    col = input(f"Player {current_player}, enter a column(1-3):")
    row = int(row) - 1
    col = int(col) - 1

    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid input")
        continue

    if board[row][col] == '':

        board[row][col] = current_player
        print(f"Player {current_player} placed an {current_player} at ({row + 1}, {col + 1})")



        if is_board_full():
            print("Board is full,its a Tie!!!")
            break

        pretty_board()

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

    else:
        print("Spot already used, choose a different spot!")
        continue
