import socket
from _thread import *
import random
from game import Game
import sys
clientNumber = 0
gameDict = {}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
clientFillList = []
try:
    s.bind((socket.gethostbyname(socket.gethostname()), 80))
    print(socket.gethostbyname(socket.gethostname()))
except socket.error as e:
    print(e)
s.listen()
print('Waiting for connection')
games = {}
def threaded_client(conn,clientNumber,gameId,color,p):
    print(1)
    conn.send(str.encode(str(clientNumber)+" " + color))
    reply = ""
    game = games[gameId]
    data = conn.recv(2000).decode("utf-8")
    game.gameRules.append(data.split(","))
    conn.sendall(str.encode("starting"))
    if p==1:
        game.started =True
        game.decideRules()
    firstflag = 0
    while True:
        try:
            data = conn.recv(2000).decode("utf-8")
            if data == "starting" and firstflag == 0:
                firstflag = 1
            elif firstflag==0 and data !="starting":
                conn.close
            if gameId in games:
                game = games[gameId]
                if not data:
                    print("Disconnect")
                    games.pop(gameId,None)
                    print(games)
                    break
                else:
                    if data=="starting":
                        if game.started == True:
                            reply = game.gameRules
                        else:
                            reply = "starting"
                    elif data == "waiting1":
                        if game.turn == color:
                            reply = game.last_move
                        else:
                            reply = "waiting1"

                    elif data != "waiting1" and data != "myturn":
                        print("67 ")
                        game.last_move = data
                        reply = "waiting1"
                        game.update_turn()
                    elif data == "myturn":
                        reply ="myturn"
                    else:
                        reply = " "
                    print("recived : ", data, color)
                    print("sending : ", reply, color)
                conn.sendall(str.encode((str(reply))))
            else:
                conn.close
        except:
            break
    print("Lost Connection")
    conn.close

while True:
    conn, addr = s.accept()
    clientNumber += 1
    gameId = (clientNumber - 1) // 2
    if clientNumber % 2 == 1:
        color = random.choice(("black", "white"))
        if color == "white":
            games[gameId] = Game(gameId)
            nextColor = "black"
        else:
            games[gameId] = Game(gameId)
            nextColor = "white"
        start_new_thread(threaded_client, (conn, clientNumber, gameId, color,0))


    else:
        start_new_thread(threaded_client, (conn, clientNumber, gameId, nextColor,1))
def get_move_from_data(data):
    newData = data.split(",")
    return newData
