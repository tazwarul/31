def print_board(board):
    print("\n")
    print(" " + board[0]+ " | " + board[1]+" | "+ board[2])
    print("---+---+---")
    print(" " + board[3]+ " | " + board[4]+" | "+ board[5])
    print("---+---+---")
    print(" " + board[6]+ " | " + board[7]+" | "+ board[8])
    print("---+---+---")

def check_winner(board, player):
    win_condition= [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_condition:
        if board[condition[0]]== board[condition[1]]==board[condition[2]]==player:
            return True
    return False

def tic_tac_toe():
    board = [" "]*9
    current_player= "X"
    moves_X = []  # Track moves for X
    moves_O = []  # Track moves for O

    print("Welcome to Tic Tac Toe! (Max 3 moves per player)")
    print_board(board)

    while True:
        try:
            move=int(input(f"Player {current_player}, choose a position (1-9): "))-1 

            if move < 0 or move > 8:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            if board[move] == " ":
                # Decide which move list to use
                moves_queue = moves_X if current_player == "X" else moves_O

                # Remove oldest move if player already has 3 moves
                if len(moves_queue) == 3:
                    old_move = moves_queue.pop(0)
                    board[old_move] = " "
                    print(f"Player {current_player}'s first move at position {old_move+1} withdrawn!")

                # Make the new move
                board[move] = current_player
                moves_queue.append(move)
                print_board(board)

                # Check winner
                if check_winner(board,current_player):
                    print(f"Player {current_player} wins!")
                    break

                # Switch player
                current_player="O" if current_player=="X" else "X"

            else:
                print("That spot is already taken, try again.")

        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")

# Run the game
tic_tac_toe()
