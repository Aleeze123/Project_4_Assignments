import random
from termcolor import colored
def print_board(board):
    print(colored(f"{board[0]} | {board[1]} | {board[2]}", 'yellow'))
    print(colored("---------", 'yellow'))
    print(colored(f"{board[3]} | {board[4]} | {board[5]}", 'yellow'))
    print(colored("---------", 'yellow'))
    print(colored(f"{board[6]} | {board[7]} | {board[8]}", 'yellow'))
def check_win(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]            
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == player:
            return True
    return False
def check_draw(board):
    return ' ' not in board
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'X'):
        return -1
    if check_win(board, 'O'):
        return 1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
def get_best_move(board):
    best_move = -1
    best_value = float('-inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_value = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move
def player_turn(board):
    while True:
        try:
            position = int(input(colored("Player X, choose a position (1-9): ", 'cyan'))) - 1
            if board[position] == ' ':
                board[position] = 'X'
                break
            else:
                print(colored("That spot is taken, choose a different one.", 'red'))
        except (ValueError, IndexError):
            print(colored("Invalid input. Please choose a number between 1 and 9.", 'red'))
def computer_turn(board):
    print(colored("Computer is thinking...", 'green'))
    move = get_best_move(board)
    board[move] = 'O'
    print(colored(f"Computer chose position {move + 1}.", 'green'))
def main():
    board = [' '] * 9
    current_player = 'X'

    print(colored("Welcome to Tic-Tac-Toe against AI!", 'cyan'))
    print_board(board)

    while True:
        if current_player == 'X':
            player_turn(board)
        else:
            computer_turn(board)

        print_board(board)

        if check_win(board, 'X'):
            print(colored("Player X wins!", 'green'))
            break

        if check_win(board, 'O'):
            print(colored("Computer (Player O) wins!", 'green'))
            break

        if check_draw(board):
            print(colored("It's a draw!", 'yellow'))
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
