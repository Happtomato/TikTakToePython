def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    print_board(board)
    while True:
        try:
            row = int(input("Enter row number (0-2) for player {}: ".format(player)))
            col = int(input("Enter column number (0-2) for player {}: ".format(player)))
        except ValueError:
            print("Invalid input, please enter a number between 0 and 2.")
            continue
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input, please enter a number between 0 and 2.")
            continue
        if board[row][col] != " ":
            print("Invalid move, that position is already taken. Please try again.")
            continue
        board[row][col] = player
        print_board(board)
        if check_win(board, player):
            print("Player {} wins!".format(player))
            break
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("Game over, it's a tie!")
            break
        player = "O" if player == "X" else "X"

play_game()
