import socket
import threading
import pickle

host = '127.0.0.1'
port = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

players = []

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

def handle_client(client, player):
    global players
    while True:
        try:
            data = client.recv(2048)
            if not data:
                break
            players = pickle.loads(data)
            send_to_clients()
        except:
            break
    client.close()

def send_to_clients():
    for player_data in players:
        for client in player_data['clients']:
            data = pickle.dumps(players)
            client.send(data)

def start():
    while True:
        client, address = server.accept()
        print(f"New connection: {address}")

        if len(players) % 2 == 0:
            new_player = Player(100, 100, (255, 0, 0))
        else:
            new_player = Player(200, 100, (0, 255, 0))

        players.append({'player': new_player, 'clients': [client]})

        thread = threading.Thread(target=handle_client, args=(client, new_player))
        thread.start()

print("Server is running...")
start()
