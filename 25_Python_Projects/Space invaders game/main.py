import pygame
import random
import sys
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 7
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.rect.y = random.randint(-50, -10)
            self.rect.x = random.randint(0, screen_width - 50)
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(5):
    for j in range(5):
        enemy = Enemy(50 + i * 100, 50 + j * 60)
        all_sprites.add(enemy)
        enemies.add(enemy)
running = True
game_over = False
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
    all_sprites.update()
    for bullet in bullets:
        enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)
        for enemy in enemies_hit:
            bullet.kill()
    if pygame.sprite.spritecollide(player, enemies, False):
        game_over = True
    screen.fill(BLACK)
    all_sprites.draw(screen)
    if game_over:
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
    pygame.display.flip()
pygame.quit()
sys.exit()
