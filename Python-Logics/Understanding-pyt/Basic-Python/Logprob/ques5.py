import random

# Create board
board = [" " for _ in range(9)]

def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board


print("Tic Tac Toe Game Start!")
print_board()

while True:
    # User Move
    move = int(input("Enter position (0-8): "))
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Cell already taken!")
        continue

    print_board()

    if check_winner("X"):
        print("You Win!")
        break
    if is_draw():
        print("Draw!")
        break

    # Computer Move
    while True:
        comp_move = random.randint(0, 8)
        if board[comp_move] == " ":
            board[comp_move] = "O"
            break

    print("Computer chose:", comp_move)
    print_board()

    if check_winner("O"):
        print("Computer Wins!")
        break
    if is_draw():
        print("Draw!")
        break