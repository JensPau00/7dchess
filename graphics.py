import rules
import pygame
import math
mainMenuButtons = []
from network import breakList
current5Slice = 0
current6Slice = 0
mouseHeld = 0
dim = 0
mode = 0
imageDict={}
imageDict[('black', 'Bishop')] = pygame.image.load('BlackBishop.png')
imageDict[('white', 'Bishop')] = pygame.image.load('WhiteBis.png')
imageDict[('white', 'ArchBishop')] = pygame.image.load('WhiteArch.png')
imageDict[('white', 'NightMare')] = pygame.transform.flip(pygame.image.load('WhiteNight.png'), 1, 0)
imageDict[('white', 'Pope')] = pygame.image.load('WhitePope.png')
imageDict[('black', 'ArchBishop')] = pygame.image.load('BlackArch.png')
imageDict[('black', 'Pope')] = pygame.image.load('BlackPope.png')
imageDict[('black', 'King')] = pygame.image.load('BlackKing.png')
imageDict[('black', 'Queen')] = pygame.image.load('BlackQueen.png')
imageDict[('black', 'Rook')] = pygame.image.load('BlackRook.png')
imageDict[('black', 'Knight')] = pygame.image.load('BlackKnight.png')
imageDict[('black', 'NightMare')] = pygame.image.load('BlackNight.png')
imageDict[('white', 'Pawn')] = pygame.image.load('WhitePawn.png')
imageDict[('white', 'King')] = pygame.image.load('WhiteKing.png')
imageDict[('white', 'Queen')] = pygame.image.load('WhiteQueen.png')
imageDict[('white', 'Rook')] = pygame.image.load('WhiteRook.png')
imageDict[('white', 'Knight')] = pygame.transform.flip(pygame.image.load('WhiteKnight.png'), 1, 0)
imageDict[('black', 'Pawn')] = pygame.image.load('BlackPawn.png')
flag = 0
prevList = []
currList = []
for each in range(rules.numberOfDimensions):
    prevList.append(0)
class runGraphics():
    def __init__(self, resolution):
        pygame.init()
        
        global square_size
        self.res = resolution
        self.screen = pygame.display.set_mode(resolution)
        square_size = int(resolution[1] / rules.size/(rules.size+1))
        self.clock = pygame.time.Clock()
    def draw_piece(self, picture, location,color,each=0):
        if rules.numberOfDimensions==6:
            condition = current6Slice == location[5] and current5Slice == location[4]
        elif rules.numberOfDimensions==5:
            condition = current5Slice == location[4]
        else:
                condition = True
        if condition and each ==0:
            try:
                image = imageDict[(color,picture)]
            except:
                image = pygame.image.load('WhiteBis.png')
            image = pygame.transform.scale(image,(square_size,square_size))
            if each == 0:
                self.screen.blit(image,(location[1]*square_size+location[3]*square_size*(rules.size+1),location[0]*square_size+location[2]*square_size*(rules.size+1)))
        elif each != 0:
            image = imageDict[(color, picture)]
            image = pygame.transform.scale(image, (square_size, square_size))
            mouse = pygame.mouse.get_pos()
            self.screen.blit(image,(mouse[0]-square_size/2,mouse[1]-square_size/2))
            pygame.mouse.set_visible(False)
    def draw_board(self):
        self.screen.fill((125, 125, 255))
        for x in range(1,rules.size+1):
            for y in range(1,rules.size+1):
                for z in range(1,rules.size+1):
                    for w in range(1,rules.size+1):
                        pattern2 = (x%2 == 1 and y%2 != 1) or (x%2 != 1 and y%2 == 1)
                        pattern3 = (w%2 == 0 and z%2 != 0) or (w%2 != 0 and z%2 == 0)
                        pattern4 = ((current5Slice+current6Slice)%2 == 0)
                        rect = ((y - 1) * square_size + (w - 1) * square_size * (rules.size+1), (x - 1) * square_size +(z - 1)* square_size * (rules.size+1), square_size, square_size)
                        if (not pattern2 and pattern3 and pattern4) :
                            pygame.draw.rect(self.screen,(125,0,0),rect)
                        elif (pattern2 and pattern3 and pattern4):
                            pygame.draw.rect(self.screen, (0, 125, 0), rect)
                        elif (pattern2 and not pattern3 and pattern4):
                            pygame.draw.rect(self.screen, (125, 0, 0), rect)
                        elif (not pattern2 and not pattern3 and pattern4):
                            pygame.draw.rect(self.screen,(0,125,0),rect)
                        elif (not pattern2 and pattern3 and not pattern4) :
                            pygame.draw.rect(self.screen,(0,125,0),rect)
                        elif (pattern2 and pattern3 and not pattern4):
                            pygame.draw.rect(self.screen, (125, 0, 0), rect)
                        elif (pattern2 and not pattern3 and not pattern4):
                            pygame.draw.rect(self.screen, (0, 125, 0), rect)
                        else:
                            pygame.draw.rect(self.screen,(125,0,0),rect)
    def draw_legal_moves(self,piece):
        piece.find_moves()
        for each in piece.legal_moves:
            print(1)
            if rules.numberOfDimensions == 6:
                condition = current5Slice == each[4] and current6Slice == each[5]
            elif rules.numberOfDimensions == 5:
                condition = current5Slice == each[4]
            else:
                condition = True
            if condition:
                circle = ((each[1] ) * square_size + (each[3] ) * square_size * (rules.size+1)+int(square_size/2), (each[0]) * square_size +(each[2])* square_size * (rules.size+1)+int(square_size/2))
                pygame.draw.circle(self.screen, (255, 255, 0), circle,int(square_size/5))
    def update(self,color,phase,data):
        if phase == 0:
            self.clock.tick(60)
            self.screen.fill(0)
            self.draw_board()
            font = pygame.font.SysFont("Comic Sans MS", 20)
            font = font.render("WAITING FOR ANOTHER COOMER",True,(255,255,255))
            self.screen.blit(font, (self.res[0]//2, self.res[1]//2))
            if data != "starting":
                if color  == "white":
                    data = "myturn"
                    print("here")
                else:
                    data = "waiting1"
                    print("not Here")
            pygame.display.flip()
            return data
        else:
            flagg = 1
            information = ""
            if data != "myturn" and data != "waiting1":
                data = breakList(data,rules.numberOfDimensions)
                data = data.split(",")
                prevListData = []
                moveTo = []
                for index, each in enumerate(data):
                    for all in each:
                        try:
                            int(all)
                            if index == 0:
                                prevListData.append(int(all))
                            if index == 1:
                                moveTo.append(int(all))
                        except:
                            pass
                    try:
                        rules.pieceDict[tuple(prevListData)].find_moves()
                        rules.pieceDict[tuple(prevListData)].move((moveTo))
                    except:
                        pass
                data = "myturn"
            global current5Slice,mouseHeld, current6Slice
            self.clock.tick(60)
            self.screen.fill(0)
            self.draw_board()
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]
            v = current5Slice
            u = current6Slice
            z = math.floor(y / int(square_size * (rules.size + 1)))
            w = math.floor(x / int(square_size * (rules.size + 1)))
            y = math.floor(((x - w * square_size * (rules.size + 1))) / square_size) % (rules.size+1)
            x = math.floor(((mouse[1] - z * square_size * (rules.size + 1))) / square_size) % (rules.size+1)
            if rules.numberOfDimensions == 6:
                coordlist =[x,y,z,w,v,u]
            elif rules.numberOfDimensions == 5:
                coordlist =[x,y,z,w,v]
            else:
                coordlist = [x,y,z,w]
            mouseHeld = 0
            for event in pygame.event.get():
                # quit if the quit button was pressed
                global flag
                for each in rules.pieceList:
                    each.location
                if event.type == pygame.QUIT:
                    exit()
                keys=pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    current5Slice += 1
                    if current5Slice > rules.size-1:
                        current5Slice = rules.size-1
                if keys[pygame.K_DOWN]:
                    current5Slice -= 1
                    if current5Slice<0:
                        current5Slice = 0
                if keys[pygame.K_LEFT]:
                    current6Slice -= 1
                    if current6Slice < 0:
                        current6Slice = 0
                if keys[pygame.K_RIGHT]:
                    current6Slice += 1
                    if current6Slice > rules.size - 1:
                        current6Slice = rules.size - 1
            mousebuttons = pygame.mouse.get_pressed()
            if mousebuttons[0] == 1:
                mouseHeld = 1
                if flag == 0:
                     try:
                        print(rules.pieceDict, rules.pieceList)
                        if rules.pieceDict[tuple(coordlist)].color == color:
                            rules.pieceDict[tuple(coordlist)].grabbed = 1
                            for each in range(len(prevList)):
                                prevList[each] = coordlist[each]
                            flag = 1
                     except:
                        pass
            if flag == 1 and mouseHeld == 0:
                flag = 0
                try:
                    rules.pieceDict[tuple(prevList)].grabbed = 0
                    if data == "myturn":
                        rules.pieceDict[tuple(prevList)].move(coordlist)
                        information = str([prevList,coordlist,color])
                        if list(prevList) == list(coordlist):
                            information = ""
                            print('fail')
                        else:
                            flagg=1
                            print("suces")

                except:
                    pass
            grabbedFlag = 0
            draw = 0
            for each in rules.pieceList:
                if not each.grabbed:
                    self.draw_piece(each.image, each.location, each.color)
                if each.grabbed:
                    draw = each
                    self.draw_piece(each.image, each.location, each.color,each)
                    grabbedFlag = 1
            if draw != 0:
                self.draw_legal_moves(draw)
            if grabbedFlag == 1:
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            font = pygame.font.SysFont("Comic Sans MS", 16)
            font = font.render(str(current5Slice) + "," + str(current6Slice), True, (0, 0, 0))
            self.screen.blit(font, (1400, 100))
            if data =="waiting1" and information == "":
                information = "waiting1"
            elif data == "myturn" and information == "":
                information = "myturn"
            pygame.display.flip()
            king_alive = 0
            for each in rules.pieceList:
                if type(each) == rules.King and color != each.color:
                    king_alive = 1
            if king_alive == 0:
                information = 'win'
            if flagg == 1:

                print(information)
            return information

    def offline(self):
        global current5Slice, mouseHeld, current6Slice
        self.clock.tick(60)
        self.screen.fill(0)
        self.draw_board()
        mouse = pygame.mouse.get_pos()
        mouseHeld = 0
        for event in pygame.event.get():
            # quit if the quit button was pressed
            global flag
            for each in rules.pieceList:
                each.location
            if event.type == pygame.QUIT:
                rules.clearBoard()
                pygame.display.quit()
                pygame.quit()
                return False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                current5Slice += 1
                if current5Slice > rules.size - 1:
                    current5Slice = rules.size - 1
            if keys[pygame.K_DOWN]:
                current5Slice -= 1
                if current5Slice < 0:
                    current5Slice = 0
            if keys[pygame.K_LEFT]:
                current6Slice -= 1
                if current6Slice < 0:
                    current6Slice = 0
            if keys[pygame.K_RIGHT]:
                current6Slice += 1
                if current6Slice > rules.size - 1:
                    current6Slice = rules.size - 1
        x = mouse[0]
        y = mouse[1]
        v = current5Slice
        u = current6Slice
        z = math.floor(y / int(square_size * (rules.size + 1)))
        w = math.floor(x / int(square_size * (rules.size + 1)))
        y = math.floor(((x - w * square_size * (rules.size + 1))) / square_size) % (rules.size + 1)
        x = math.floor(((mouse[1] - z * square_size * (rules.size + 1))) / square_size) % (rules.size + 1)
        if rules.numberOfDimensions == 6:
            coordlist = [x, y, z, w, v, u]
        elif rules.numberOfDimensions == 5:
            coordlist = [x, y, z, w, v]
        else:
            coordlist = [x, y, z, w]
        mousebuttons = pygame.mouse.get_pressed()
        if mousebuttons[0] == 1:
            mouseHeld = 1
            if flag == 0:
                try:
                    rules.pieceDict[tuple(coordlist)].grabbed = 1
                    for each in range(len(prevList)):
                        prevList[each] = coordlist[each]
                        print('succ')
                    print(prevList,coordlist)
                    flag = 1
                except:
                    print(coordlist)
        if flag == 1 and mouseHeld == 0:
            flag = 0
            try:
                rules.pieceDict[tuple(prevList)].grabbed = 0
                rules.pieceDict[tuple(prevList)].move(coordlist)
            except:
                print(coordlist)
        grabbedFlag = 0
        draw = 0
        for each in rules.pieceList:
            if not each.grabbed:
                self.draw_piece(each.image, each.location, each.color)
            if each.grabbed:
                draw = each
                self.draw_piece(each.image, each.location, each.color, each)
                grabbedFlag = 1
        if draw != 0:
            self.draw_legal_moves(draw)
        if grabbedFlag == 1:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)
        font = pygame.font.SysFont("Comic Sans MS", 16)
        font = font.render(str(current5Slice)+","+str(current6Slice), True, (0, 0, 0))
        self.screen.blit(font,(1400,100))
        pygame.display.flip()
        return True


class Button:
    def __init__(self,text,size,location,color,typeOfButton):
        self.text = text
        self.size = size
        self.location = location
        self.color = color
        self.typeOf = typeOfButton
        self.rect = pygame.Rect(location[0], location[1],size[0],size[1])
        self.selected = 0
        self.pressed = 0
    def inside(self,pos):
        return self.rect.collidepoint(pos)
    def imageArg(self,surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.SysFont("Comic Sans MS", 12)
        font = font.render(self.text,True,(0,0,0))
        surface.blit(font, (self.location[0]+((self.size[0]-font.get_width())//2), self.location[1]+((self.size[1]-font.get_height()))//2))

mainMenuButtons.append(Button("4-D Chess",(67,100),(500,500),(255,0,0),"Dim"))
mainMenuButtons.append(Button("5-D Chess",(66,100),(567,500),(255,0,0),"Dim"))
mainMenuButtons.append(Button("6-D Chess",(67,100),(633,500),(255,0,0),"Dim"))
mainMenuButtons.append(Button("Assimilation",(100,100),(600,600),(255,0,0),"Mode"))
mainMenuButtons.append(Button("Normal",(100,100),(500,600),(255,0,0),"Mode"))
mainMenuButtons.append(Button("Search",(100,100),(500,700),(255,0,0),"Start"))
mainMenuButtons.append(Button("Practice",(100,100),(600,700),(255,0,0),"Start"))


