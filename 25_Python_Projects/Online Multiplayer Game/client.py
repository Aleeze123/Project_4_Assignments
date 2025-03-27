import socket
import pygame
import pickle

host = '127.0.0.1'
port = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Online Multiplayer Game")

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = 5

player = Player(100, 100, (255, 0, 0))

def send_data():
    try:
        players_data = pickle.dumps([player])
        client.send(players_data)
    except:
        pass

def receive_data():
    global player
    while True:
        try:
            data = client.recv(2048)
            players = pickle.loads(data)
            if len(players) > 0:
                draw_window(players)
        except:
            pass

def update():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= player.velocity
        if keys[pygame.K_RIGHT]:
            player.x += player.velocity
        if keys[pygame.K_UP]:
            player.y -= player.velocity
        if keys[pygame.K_DOWN]:
            player.y += player.velocity

        send_data()

    pygame.quit()

def draw_window(players):
    win.fill((0, 0, 0))
    for player_data in players:
        pygame.draw.rect(win, player_data['player'].color, (player_data['player'].x, player_data['player'].y, 50, 50))
    pygame.display.update()

import threading
receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

update()
