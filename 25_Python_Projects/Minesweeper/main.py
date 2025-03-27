import random
import sys
from termcolor import colored

class Minesweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.visible = [[' ' for _ in range(width)] for _ in range(height)]
        self.mines = set()
        self.game_over = False

    def generate_mines(self):
        while len(self.mines) < self.num_mines:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if (x, y) not in self.mines:
                self.mines.add((x, y))
                self.board[y][x] = 'X'

    def count_adjacent_mines(self, x, y):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx] == 'X':
                    count += 1
        return count

    def reveal(self, x, y):
        if self.visible[y][x] != ' ' or self.board[y][x] == 'X':
            return

        adjacent_mines = self.count_adjacent_mines(x, y)
        if adjacent_mines > 0:
            self.visible[y][x] = str(adjacent_mines)
        else:
            self.visible[y][x] = '.'
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and self.visible[ny][nx] == ' ':
                        self.reveal(nx, ny)

    def display(self):
        print('   ' + ' '.join([str(i) for i in range(self.width)]))
        for y in range(self.height):
            row = f"{y}  "
            for x in range(self.width):
                if self.visible[y][x] == 'X':
                    row += colored(self.visible[y][x], 'red') + ' '
                elif self.visible[y][x] == '.':
                    row += colored(self.visible[y][x], 'grey') + ' '
                elif self.visible[y][x] == ' ':
                    row += colored(self.visible[y][x], 'cyan') + ' '
                else:
                    row += colored(self.visible[y][x], 'yellow') + ' '
            print(row)

    def play(self):
        self.generate_mines()
        while not self.game_over:
            self.display()
            try:
                x, y = map(int, input("Enter x and y coordinates (separated by space): ").split())
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(colored("Out of bounds, try again!", 'yellow'))
                    continue
                if self.board[y][x] == 'X':
                    self.game_over = True
                    self.visible[y][x] = 'X'
                    print(colored("Game Over! You hit a mine!", 'red'))
                else:
                    self.reveal(x, y)
            except ValueError:
                print(colored("Invalid input, please enter numbers separated by space.", 'yellow'))

if __name__ == "__main__":
    game = Minesweeper(8, 8, 10)
    game.play()
