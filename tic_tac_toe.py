import random

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * (4 * len(board) - 1))
    print()

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(len(board))) or \
       all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[i][len(board)-1-i] != ' ' for i in range(len(board))):
        return True

    return False


def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if check_winner(board):
        return -1 if maximizing_player else 1
    if is_board_full(board):
        return 0

    empty_cells = get_empty_cells(board)

    if maximizing_player:
        max_eval = float('-inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            eval = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            eval = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval




def get_best_move(board):
    empty_cells = get_empty_cells(board)
    # Shuffle the list to avoid repetitive moves
    random.shuffle(empty_cells)  
    best_move = None
    best_eval = float('-inf')

    for cell in empty_cells:
        board[cell[0]][cell[1]] = 'O'
        eval = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = cell

    return best_move



def choose_starting_player():
    return random.choice(['X', 'O'])

def main():
    ai_wins = 0
    player_wins = 0

    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = choose_starting_player()

        while not check_winner(board) and not is_board_full(board):
            print_board(board)

            if current_player == 'X':
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    current_player = 'O'
                else:
                    print("Cell already taken. Try again.")
            else:
                print("AI's turn (O)")
                move = get_best_move(board)
                board[move[0]][move[1]] = 'O'
                current_player = 'X'

        print_board(board)

        if check_winner(board):
            winner = 'X' if current_player == 'O' else 'O'
            print(f"{winner} wins!")
            if winner == 'O':
                ai_wins += 1
            else:
                player_wins += 1
        else:
            print("It's a tie!")

        print(f"Player Wins: {player_wins}, AI Wins: {ai_wins}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break



if __name__ == "__main__":
    main()
