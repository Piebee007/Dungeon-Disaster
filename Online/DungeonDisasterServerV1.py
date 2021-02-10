import socket
from _thread import *
from ObjectCodeV6 import Player, Enemy,bulletArray, Projectile
import pickle
import time
import random
import pygame

#Details about the server
serverIp = "192.168.1.106"
port = 5555

#This creates all the socket information
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((serverIp, port))
except socket.error as e:
    str(e)

#Here the server will be waiting for clients to connect to the server. For the single game version, it is only accepting 2 connections
server_socket.listen(2)
print("Waiting for a connection, Server Started")


#Theses will be the randomly selected maps for the games
map1 = random.randint(0,2)
map2 = random.randint(0,2)
map3 = random.randint(0,2)

player_images = [[(pygame.image.load('Player1.png')),  (pygame.image.load('Player2.png')),  (pygame.image.load('Player3.png'))],[(pygame.transform.flip((pygame.image.load('Player1.png')), True, False)), (pygame.transform.flip((pygame.image.load('Player2.png')), True, False)),(pygame.transform.flip((pygame.image.load('Player3.png')), True, False))],[(pygame.image.load('Player4.png')),  (pygame.image.load('Player5.png')),  (pygame.image.load('Player6.png'))], [(pygame.image.load('Player7.png')),  (pygame.image.load('Player8.png')),  (pygame.image.load('Player9.png'))]]

#This variable stores all the data for the games
gameData = [Player(1340, 50, 50,0,1,map1, player_images, 0),Player(500, 50, 50,0,1,map1, player_images, 1)]


#This procedure is responsible for receiving data and sending data back to the client
def client_thread(conn, playerID):

    #This will be sending the starting object code to the player
    conn.send(pickle.dumps(gameData[playerID]))

    #This while loop will wait for the user to send their object code and then receive ther other player's object code
    reply = ""
    while True:
        try:
            #Receive the data
            dataReceived = pickle.loads(conn.recv(2048))
            #Update the game data
            gameData[playerID] = dataReceived
                    

            #Disconnect if there is no data being received
            if not dataReceived:

                print("Disconnected")
                break
            else:
                #Depending on the player's id, it will send a specific player object code back
                if playerID == 1:
                    reply = gameData[0]
                elif playerID == 0:
                    reply = gameData[1]

                print("Received: ", dataReceived) 
                print("Sending : ", reply)

            #Send back the object to the player
            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

#Wait for people to connect to the server
while True:
    conn, address = server_socket.accept()
    print("Connected to:", address)
    #When a user is connected, a new thread will be made
    start_new_thread(client_thread, (conn, currentPlayer))
    currentPlayer += 1
