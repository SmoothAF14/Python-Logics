import random

board = [" " for _ in range(9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(player):
    wincon = {
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    }
    for pos in wincon:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False
        
def draw():
    return " " not in board

print ("Welcome to Tic Tac Toe!")
print_board

while True:
    move = int(input("Enter your move (0-8): "))
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move, try again.")
        continue
    print_board()
    if check_win("X"):
        print("Congratulations! You win!")
        break
    if draw():
        print("It's a draw!")
        break

    while True:
        computer_move = random.randint(0, 8)
        if board[computer_move] == " ":
            board[computer_move] = "O"
            break
    print(f"Computer chose {computer_move}")
    print_board()
    if check_win("O"):
        print("Computer wins! Better luck next time.")
        break
    if draw():
        print("It's a draw!")
        break

