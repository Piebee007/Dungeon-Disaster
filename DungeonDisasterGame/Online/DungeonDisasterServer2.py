import socket
from _thread import *
from ObjectCodeV3 import *
import pickle
import time
import random

server = "192.168.1.106"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


#players = [Player(0,0,50,50,30,30), Player(100,100, 50,50, 30,30)]



map1 = random.randint(0,2)
map2 = random.randint(0,2)
map3 = random.randint(0,2)
player_images = [[(pygame.image.load('Player1.png')),  (pygame.image.load('Player2.png')),  (pygame.image.load('Player3.png'))],[(pygame.transform.flip((pygame.image.load('Player1.png')), True, False)), (pygame.transform.flip((pygame.image.load('Player2.png')), True, False)),(pygame.transform.flip((pygame.image.load('Player3.png')), True, False))],[(pygame.image.load('Player4.png')),  (pygame.image.load('Player5.png')),  (pygame.image.load('Player6.png'))], [(pygame.image.load('Player7.png')),  (pygame.image.load('Player8.png')),  (pygame.image.load('Player9.png'))]]


player_data = [Player(1340, 50, 50,0,1,map1, player_images),Player(500, 50, 50,0,1,map1, player_images)]


def threaded_client(conn, player):
    
    conn.send(pickle.dumps(player_data[player]))
    
    
    reply = ""
    
    
    while True:
        
        
        try:
            data = pickle.loads(conn.recv(2048))
            player_data[player] = data
                    


            if not data:

                print("Disconnected")
                break
            else:
                
                if player == 1:
                    reply = player_data[0]
                elif player == 0:
                    reply = player_data[1]



                print("Received: ", data) 
                print("Sending : ", reply)





            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, address = s.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
