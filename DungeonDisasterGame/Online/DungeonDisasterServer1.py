import socket
from _thread import *
import pickle
import time
import random
from ObjectCode import * #This is a module that will be used to create the players and enemies

server = "192.168.1.106"
port = 5555
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server, port))
except socket.error as e:
    str(e)

max_people = 2
server_socket.listen(max_people)

map1 = random.randint(0,2)
map2 = random.randint(0,2)
map3 = random.randint(0,2)
player_images = [[(pygame.image.load('Player1.png')),  (pygame.image.load('Player2.png')),  (pygame.image.load('Player3.png'))],[(pygame.transform.flip((pygame.image.load('Player1.png')), True, False)), (pygame.transform.flip((pygame.image.load('Player2.png')), True, False)),(pygame.transform.flip((pygame.image.load('Player3.png')), True, False))],[(pygame.image.load('Player4.png')),  (pygame.image.load('Player5.png')),  (pygame.image.load('Player6.png'))], [(pygame.image.load('Player7.png')),  (pygame.image.load('Player8.png')),  (pygame.image.load('Player9.png'))]]


game_data = [Player(1340, 50, 50,0,1,map1, player_images),Player(500, 50, 50,0,1,map1, player_images)]

def client_thread(connection,player_id):
    print("yes")
    connection.send(pickle.dumps(game_data[player_id]))
    print(game_data[player_id])
    reply = ""

    while True:

        try:
            dataReceived = pickle.loads(connection.recv(4096))
            game_data[player_id] = dataReceived

            if not data:
                print("Player" + str(player_id) + "has disconnected")
                break
            else:

                if player_id == 0:
                    reply = game_data[1]
                elif player_id == 1:
                    reply = game_data[0]

                print("Received: ", dataReceived)
                print("Reply: ", reply)
                connection.sendall(pickle.dumps(reply))
                
        except:
            break

    print("Lost connection")
    connection.close
                
                    
def main_loop():
    currentPlayer = 0
        #####Change connection to conn
    connection, address = server_socket.accept()
    print("Connected to: ", address)

    start_new_thread(client_thread,(connection,currentPlayer))

    currentPlayer += 1

main_loop()
