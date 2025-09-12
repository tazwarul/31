# Tic Tac Toe Game in Python

def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    # All possible winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_full(board):
    return " " not in board

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
                print_board(board)

                if check_winner(board, current_player):
                    print(f"🎉 Player {current_player} wins!")
                    break
                elif is_full(board):
                    print("It's a draw!")
                    break

                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")

# Run the game
tic_tac_toe()
