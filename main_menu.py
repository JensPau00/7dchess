import pygame
mainMenuButtons = []
import sys

class runGraphics():
    def __init__(self, resolution):
        pygame.init()
        self.res = resolution
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.dim = 4
        self.size = 4
        self.mode = 'Normal'
        mainMenuButtons.append(Button("4-D Chess", (67, 67), ((self.res[0]//2-100), 515), (255, 0, 0), (200, 0, 100), "Dim"))
        mainMenuButtons.append(Button("5-D Chess", (66, 67), ((self.res[0]//2-32), 515), (255, 0, 0), (200, 0, 100), "Dim"))
        mainMenuButtons.append(Button("6-D Chess", (67, 67), ((self.res[0]//2+35), 515), (255, 0, 0), (200, 0, 100), "Dim"))
        mainMenuButtons.append(Button("Assimilation", (100, 100), ((self.res[0]//2-101), 600), (255, 0, 0), (200, 0, 100), "Mode"))
        mainMenuButtons.append(Button("Normal", (100, 100), ((self.res[0]//2+1), 600), (255, 0, 0), (200, 0, 100), "Mode"))
        mainMenuButtons.append(Button("Search", (100, 100), ((self.res[0]//2-101), 720), (255, 0, 0), (200, 0, 100), "Start"))
        mainMenuButtons.append(Button("Practice", (100, 100), ((self.res[0]//2+1), 720), (255, 0, 0), (200, 0, 100), "Start"))
        mainMenuButtons.append(Button("Exit", (100, 100), (0, 0), (255, 0, 0), (200, 0, 100), "Leave"))
        mainMenuButtons.append(Button("Size: 4", (50, 50), ((self.res[0]//2-150), 450), (255, 0, 0), (200, 0, 100), "Size"))
        mainMenuButtons.append(Button("Size: 5", (50, 50), ((self.res[0]//2-90), 450), (255, 0, 0), (200, 0, 100), "Size"))
        mainMenuButtons.append(Button("Size: 6", (50, 50), ((self.res[0]//2-30), 450), (255, 0, 0), (200, 0, 100), "Size"))
        mainMenuButtons.append(Button("Size: 7", (50, 50), ((self.res[0]//2+30), 450), (255, 0, 0), (200, 0, 100), "Size"))
        mainMenuButtons.append(Button("Size: 8", (50, 50), ((self.res[0]//2+90), 450), (255, 0, 0), (200, 0, 100), "Size"))
    def main_menu(self):
        self.clock.tick(60)
        self.screen.fill((50, 50, 50))
        findGame = False
        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()
        start = True
        font = pygame.font.SysFont("Comic Sans MS", 20)
        font = font.render(f'WELCOME TO ND CHESS, GAMER. SELECT THE MODE, AND THE NUMBER OF DIMENSIONS.', True,
                           (255, 255, 0))
        self.screen.blit(font, ((self.res[0]-font.get_width())//2,100))
        mouse = pygame.mouse.get_pos()
        for each in mainMenuButtons:
            each.imageArg(self.screen)
            bean = each.inside(mouse)
            mousePress = pygame.mouse.get_pressed()
            if mousePress[0] and each.inside(mouse):
                if each.text == "4-D Chess" and each.typeOf == "Dim":
                    self.dim = 4
                if each.text == "5-D Chess" and each.typeOf == "Dim":
                    self.dim = 5
                if each.text == "6-D Chess" and each.typeOf == "Dim":
                    self.dim = 6
                if each.text == "Assimilation" and each.typeOf == "Mode":
                    self.mode = 'assim'
                if each.text == "Normal" and each.typeOf == "Mode":
                    self.mode = 'Normal'
                if each.text == "Search" and each.typeOf == "Start":
                    start = False
                    findGame = True
                if each.text == "Practice" and each.typeOf == "Start":
                    start = False
                    findGame = False
                if each.typeOf == "Size":
                    self.size = int(each.text.split(" ")[1]) #set the size to the first value after the \s
                if each.typeOf =="Leave":
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
        font = pygame.font.SysFont("Comic Sans MS", 20)
        textString = "Size = "+str(self.size)+". The mode is "+str(self.mode)+". The Number of Dimensions are "+str(self.dim)+"!"
        font = font.render(textString, True,
                           (255, 255, 0))
        font.get_width()
        self.screen.blit(font, (((self.res[0]-font.get_width())//2), 300))
        pygame.display.flip()
        if start == False:
            pygame.display.quit()
            pygame.quit()
        return start, findGame,self.dim, self.mode, self.size
class Button:
    def __init__(self,text,size,location,color,insideColor,typeOfButton):
        self.text = text
        self.size = size
        self.location = location
        self.color = color
        self.OriginalColor = color
        self.typeOf = typeOfButton
        self.rect = pygame.Rect(location[0], location[1],size[0],size[1])
        self.selected = 0
        self.pressed = 0
        self.insideColor = insideColor
    def inside(self,pos):
        inside = self.rect.collidepoint(pos)
        if inside:
            self.color = self.insideColor
        else:
            self.color = self.OriginalColor
        return inside
    def imageArg(self,surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.SysFont("Comic Sans MS", 12)
        font = font.render(self.text,True,(0,0,0))
        surface.blit(font, (self.location[0]+((self.size[0]-font.get_width())//2), self.location[1]+((self.size[1]-font.get_height()))//2))

