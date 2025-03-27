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
def player_turn(board, player):
    while True:
        try:
            position = int(input(colored(f"Player {player}, choose a position (1-9): ", 'cyan'))) - 1
            if board[position] == ' ':
                board[position] = player
                break
            else:
                print(colored("That spot is taken, choose a different one.", 'red'))
        except (ValueError, IndexError):
            print(colored("Invalid input. Please choose a number between 1 and 9.", 'red'))

# Function to handle the computer's turn
def computer_turn(board, player):
    available_positions = [i for i in range(9) if board[i] == ' ']
    position = random.choice(available_positions)
    board[position] = player
    print(colored(f"Computer chose position {position + 1}.", 'green'))
def main():
    board = [' '] * 9
    current_player = 'X'
    
    print(colored("Welcome to Tic-Tac-Toe!", 'cyan'))
    print_board(board)
    while True:
        if current_player == 'X':
            player_turn(board, current_player)
        else:
            computer_turn(board, current_player)

        print_board(board)

        if check_win(board, current_player):
            print(colored(f"Player {current_player} wins!", 'green'))
            break

        if check_draw(board):
            print(colored("It's a draw!", 'yellow'))
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
