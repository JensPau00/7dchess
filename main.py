import network
import main_menu as b
import NewBoard
import graphics
play = True
online = False
list1 = []
while True:
    m = b.runGraphics((1000, 1000))
    while play:
        list1 = m.main_menu()
        play = list1[0]
    online = list1[1]
    size = list1[4]
    dim = list1[2]
    gameMode = list1[3]
    play = True
    NewBoard.rules.numberOfDimensions = dim
    NewBoard.rules.gameMode = gameMode
    NewBoard.rules.size = size
    r = graphics.runGraphics((1000, 1000))

    if online:
        try:
            n = network.Network()
        except:
            continue
        sendText = str(size)+","+str(dim)+","+str(gameMode)
        data = n.send(sendText)
        while data == 'starting':
            reply = r.update(n.getPos()[1], 0, data)
            data = n.send(reply)
        rules = data.replace(" ","")
        rules = rules.replace("""""""","")
        rules = rules.replace("'","")
        rules = rules.replace("[","")
        rules = rules.replace("]","")
        rules = rules.split(",")
        size = rules[0]
        dim = rules[1]
        gameMode = rules[2]
        NewBoard.rules.numberOfDimensions = int(dim)
        NewBoard.rules.gameMode = gameMode
        NewBoard.rules.size = int(size)
        NewBoard.createBoard()
        graphics.prevList = []
        for each in range(NewBoard.rules.numberOfDimensions):
            graphics.prevList.append(0)
        reply = r.update(n.getPos()[1], 0, data)
        data  = n.send(reply)
        graphics.square_size = int(r.res[1] / NewBoard.rules.size / (NewBoard.rules.size + 1))
        while play:
            reply = r.update(n.getPos()[1], 1, data)
            data = n.send(reply)
    else:
        NewBoard.createBoard()
        graphics.prevList = []
        for each in range(NewBoard.rules.numberOfDimensions):
            graphics.prevList.append(0)
        graphics.square_size = int(r.res[1] / NewBoard.rules.size / (NewBoard.rules.size + 1))
        while play:
            play = r.offline()
    play = True