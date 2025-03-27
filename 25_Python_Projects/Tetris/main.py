import pygame
import random

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
FPS = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]]
]

SHAPE_COLORS = [CYAN, YELLOW, GREEN, RED, BLUE, ORANGE, MAGENTA]

class Tetris:
    def __init__(self):
        self.board = [[0] * 10 for _ in range(20)]
        self.game_over = False
        self.current_shape = self.new_shape()
        self.current_position = [0, 4]
    
    def new_shape(self):
        shape = random.choice(SHAPES)
        color = SHAPE_COLORS[SHAPES.index(shape)]
        return shape, color
    
    def valid_move(self, shape, offset):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_position[1] + x + offset[1]
                    new_y = self.current_position[0] + y + offset[0]
                    if new_x < 0 or new_x >= 10 or new_y >= 20 or self.board[new_y][new_x]:
                        return False
        return True
    
    def freeze(self):
        shape, color = self.current_shape
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_position[0] + y][self.current_position[1] + x] = color
        self.clear_lines()
    
    def clear_lines(self):
        self.board = [row for row in self.board if any(cell == 0 for cell in row)]
        while len(self.board) < 20:
            self.board.insert(0, [0] * 10)
    
    def rotate(self):
        shape, color = self.current_shape
        new_shape = list(zip(*shape[::-1]))
        if self.valid_move(new_shape, (0, 0)):
            self.current_shape = new_shape, color
    
    def move(self, dx, dy):
        if self.valid_move(self.current_shape[0], (dy, dx)):
            self.current_position[0] += dy
            self.current_position[1] += dx
        elif dy:
            self.freeze()
            if self.current_position[0] == 0:
                self.game_over = True
            self.current_shape = self.new_shape()
            self.current_position = [0, 4]

def draw_board(screen, board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_shape(screen, shape, position, color):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, ((position[1] + x) * BLOCK_SIZE, (position[0] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BLACK, ((position[1] + x) * BLOCK_SIZE, (position[0] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def main():
    clock = pygame.time.Clock()
    game = Tetris()
    
    while not game.game_over:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                if event.key == pygame.K_DOWN:
                    game.move(0, 1)
                if event.key == pygame.K_UP:
                    game.rotate()
        
        draw_board(screen, game.board)
        draw_shape(screen, game.current_shape[0], game.current_position, game.current_shape[1])
        
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
