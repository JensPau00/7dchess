from itertools import permutations
from itertools import combinations
import itertools
import start
gameMode = ''
size = 4
board = {}
numberOfDimensions = 6
#location [X,y,z,w,u,v]
if True:
    pieceList = []
    bisCombos = list(combinations(range(numberOfDimensions), 2))
    ArchBisCombos = list(permutations(range(numberOfDimensions), 3))
    popeCombos = list(permutations(range(numberOfDimensions), 4))
    KnightCombos = list(permutations(range(numberOfDimensions), 2))
    NightmareCombos = list(permutations(range(numberOfDimensions), 3))
    SpectralSteedCombos = list(permutations(range(numberOfDimensions), 4))
    pieceDict = {}
    iterarg = []
    for each in range(numberOfDimensions):
        iterarg.append(range(size))
    counter = 0
    for each in itertools.product(*iterarg):
        counter += 1
        board[tuple(each)] = 0
        pieceDict[tuple(each)] = 0
    class Piece:
        def __init__(self, location, color):
            self.location = location
            self.legal_moves = []
            self.color = color
            self.grabbed = 0
            self.inherited = []
            self.firstMove = 1
            pieceList.append(self)
            pieceDict[tuple(self.location)] = self
            if self.color == 'white':
                board[tuple(location)] = 1
            if self.color == 'black':
                board[tuple(location)] = 2

        def take_piece(self):
            pieceDict[tuple(self.location)] = 0
            board[tuple(self.location)] = 0
            pieceList.remove(self)
            del self

        def move(self, location):
            if location in self.legal_moves:
                pieceDict[tuple(self.location)] = 0
                board[tuple(self.location)] = 0
                self.firstMove = 0


            if board[tuple(location)] != 0 and location in self.legal_moves:
                if self.image != pieceDict[tuple(location)].image and pieceDict[tuple(location)].image != 'King' and gameMode == 'assim':
                    self.inherited.append(classDict[pieceDict[tuple(location)].image])
                pieceDict[tuple(location)].take_piece()

            if location in self.legal_moves:
                pieceDict[tuple(location)] = self
                self.location = list(location)
                if self.color == 'white':
                    board[tuple(location)] = 1
                if self.color == 'black':
                    board[tuple(location)] = 2

    class Bishop(Piece):
        def __init__(self, location, color):
            Piece.__init__(self, location, color)
            self.image = 'Bishop'

        def find_moves(self, inh=0):
            if inh != 1:
                self.legal_moves=[]
            for each in bisCombos:
                for x in (-1,1):
                    for y in (-1,1):
                        flag = 0
                        current_location = list(self.location)
                        for check in (range(size)):
                            if flag == 0:
                                    current_location[each[0]] += x
                                    current_location[each[1]] += y
                                    try:
                                        if self.color == 'white':
                                            enemycheck = board[tuple(current_location)] == 2
                                        else:
                                            enemycheck = board[tuple(current_location)] == 1
                                        boooling = (board[tuple(current_location)] == 0 or enemycheck) and flag == 0 and current_location[each[0]-1] < size and current_location[each[1]-1] < size and current_location[each[0]-1] >= 0 and current_location[each[1]-1] >= 0
                                        if  boooling:
                                            next_location = list(current_location)
                                            if next_location not in self.legal_moves and next_location != self.location:
                                                self.legal_moves.append(next_location)
                                            if enemycheck:
                                                flag = 1
                                        else:
                                            flag = 1
                                    except KeyError:
                                        flag = 1
                            else:
                                pass
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)

    class ArchBishop(Piece):
        def __init__(self, location, color):
            Bishop.__init__(self, location, color)
            self.image = 'ArchBishop'

        def find_moves(self, inh=0):
            if inh != 1:
                self.legal_moves = []
            for each in ArchBisCombos:
                for x in (-1, 1):
                    for y in (-1, 1):
                        for z in (-1, 1):
                            flag = 0
                            current_location = list(self.location)
                            for check in (range(size)):
                                if flag == 0:
                                    current_location[each[0]] += x
                                    current_location[each[1]] += y
                                    current_location[each[2]] += z
                                    try:
                                        if self.color == 'white':
                                            enemycheck = board[tuple(current_location)] == 2
                                        else:
                                            enemycheck = board[tuple(current_location)] == 1
                                        if (board[tuple(current_location)] == 0 or enemycheck)  and flag == 0 and current_location[each[0]-1] < size and current_location[each[1]-1] < size and current_location[each[2]-1] < size and current_location[each[0]-1] >= 0 and current_location[each[1]-1] >= 0 and current_location[each[2]-1] >= 0:
                                            next_location = list(current_location)
                                            if next_location not in self.legal_moves and next_location != self.location:
                                                self.legal_moves.append(next_location)
                                            if enemycheck:
                                                flag = 1
                                        else:
                                            flag = 1
                                    except KeyError:
                                            flag = 1
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)


    class Pope(Piece):
        def __init__(self, location, color):
            ArchBishop.__init__(self, location, color)
            self.image = 'Pope'

        def find_moves(self, inh=0):
            if inh != 1:
                self.legal_moves = []
            for each in popeCombos:
                for x in (-1, 1):
                    for y in (-1, 1):
                        for z in (-1, 1):
                            for w in (-1, 1):
                                flag = 0
                                current_location = list(self.location)
                                for check in (range(size)):
                                    if flag == 0:
                                        current_location[each[0]] += x
                                        current_location[each[1]] += y
                                        current_location[each[2]] += z
                                        current_location[each[3]] += w
                                        if True:
                                            try:
                                                if self.color == 'white':
                                                    enemycheck = board[tuple(current_location)] == 2
                                                else:
                                                    enemycheck = board[tuple(current_location)] == 1
                                                if (board[tuple(current_location)] == 0 or enemycheck) and flag == 0 and current_location[each[0]-1] < size and current_location[each[1]-1] < size and current_location[each[2]-1] < size and current_location[each[3]-1] < size and current_location[each[0]-1] >= 0 and current_location[each[1]-1] >= 0 and current_location[each[2]-1] >= 0 and current_location[each[3]-1] >= 0:
                                                    next_location = list(current_location)
                                                    if next_location not in self.legal_moves and next_location != self.location :
                                                        self.legal_moves.append(next_location)
                                                    if enemycheck:
                                                        flag = 1
                                                else:
                                                    flag = 1
                                            except KeyError:
                                                flag = 1
                                        else:
                                            pass
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)


    class Knight(Piece):
        def __init__(self, location, color):
            Piece.__init__(self, location, color)
            self.image = 'Knight'

        def find_moves(self,inh=0):
            if inh ==0:
                self.legal_moves = []
            else:
                pass
            for each in KnightCombos:
                for x in [-2,2]:
                    for y in [-1,1]:
                        current_location = list(self.location)
                        current_location[each[0]] += x
                        current_location[each[1]] += y
                        try:
                            if self.color == 'white':
                                enemycheck = board[tuple(current_location)] == 2
                            else:
                                enemycheck = board[tuple(current_location)] == 1

                            if (board[tuple(current_location)] == 0 or enemycheck) and current_location[each[0] - 1] < size and current_location[each[1] - 1] < size and current_location[each[0] - 1] >= 0 and current_location[each[1] - 1] >= 0:
                                next_location = list(current_location)
                                if next_location not in self.legal_moves and  next_location != self.location:
                                    self.legal_moves.append(next_location)
                        except KeyError:
                            pass
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)


    class NightMare(Piece):
        def __init__(self, location, color):
            Knight.__init__(self, location, color)
            self.image = 'NightMare'

        def find_moves(self, inh=0):
            if inh != 1:
                self.legal_moves = []
            for each in NightmareCombos:
                if size < 5:
                    list1 = [-2,2]
                else:
                    list1 = [-3,3]
                for x in [-2, 2]:
                    for y in [-2, 2]:
                        for w in[-1, 1]:
                            current_location = list(self.location)
                            current_location[each[0]] += x
                            current_location[each[1]] += y
                            current_location[each[2]] += w
                            try:
                                if self.color == 'white':
                                    enemycheck = board[tuple(current_location)] == 2
                                else:
                                    enemycheck = board[tuple(current_location)] == 1

                                if (board[tuple(current_location)] == 0 or enemycheck) and current_location[each[0]-1] < size and current_location[each[1]-1] < size and current_location[each[2]-1] < size and current_location[each[0]-1] >= 0 and current_location[each[1]-1] >= 0 and current_location[each[2]-1] >= 0:
                                    next_location = list(current_location)
                                    if next_location not in self.legal_moves and next_location != self.location:
                                        self.legal_moves.append(next_location)
                            except KeyError:
                                pass
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)

    class SpectralSteed(Piece):
        def __init__(self, location, color):
            NightMare.__init__(self, location, color)
            self.image = 'SpectralSteed'

        def find_moves(self, inh=0):
            if inh != 1:
                self.legal_moves = []
            for each in SpectralSteedCombos:
                if size > 4:
                    list1 =[-4, 4]
                    list2 = [-3, 3]
                else:
                    list1 = [-3, 3]
                    list2 = [-2, 2]
                for x in list1:
                    for y in list2:
                        for w in[-2, 2]:
                            for z in [-1, 1]:
                                current_location = list(self.location)
                                current_location[each[0]] += x
                                current_location[each[1]] += y
                                current_location[each[2]] += w
                                current_location[each[3]] += z
                                try:
                                    if self.color == 'white':
                                        enemycheck = board[tuple(current_location)] == 2
                                    else:
                                        enemycheck = board[tuple(current_location)] == 1

                                    if (board[tuple(current_location)] == 0 or enemycheck) and current_location[each[0]-1] < size and current_location[each[1]-1] < size and current_location[each[2]-1] < size and current_location[each[3]-1] < size and current_location[each[0]-1] >= 0 and current_location[each[1]-1] >= 0 and current_location[each[2]-1] >= 0 and current_location[each[3]-1] >= 0:
                                        next_location = list(current_location)
                                        if next_location not in self.legal_moves and next_location != self.location:
                                            self.legal_moves.append(next_location)
                                except KeyError:
                                    pass
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)



    class Pawn(Piece):
        def __init__(self, location, color):
            Piece.__init__(self, location, color)
            self.image = 'Pawn'
            self.firstMove = 1

        def find_moves(self, inh=0):
            if inh != 1:
                self.legal_moves = []
            if self.color == 'white':
                if self.firstMove == 1: # looks for the pawn moving forward 1 or 2 on the first move
                    current_location = list(self.location)
                    flag = 0
                    for each in (1,2):
                        current_location[1] =self.location[1]+each
                        try:
                            if self.color == 'white':
                                enemycheck = board[tuple(current_location)] == 2
                                friendlycheck = board[tuple(current_location)] == 1
                            if not enemycheck and not friendlycheck and flag != 1:
                                next_location = list(current_location)
                                if next_location not in self.legal_moves:
                                    self.legal_moves.append(next_location)
                            else:
                                flag = 1
                        except KeyError:
                            pass
                for each in (2, 3): # Forward movement of pawns
                    current_location = list(self.location)
                    if current_location[each-1] < size-1 and each == 2:
                        current_location[each-1] += 1
                    elif each == 2 and current_location[1] == size-1:
                        current_location[3] += 1 # this checks for 4d moves
                        current_location[1] = 0
                    elif each == 3 and current_location[each-1] > 0:
                        current_location[each-1] -= 1
                    try:
                        if self.color == 'white':
                            enemycheck = board[tuple(current_location)] == 2
                            friendlycheck = board[tuple(current_location)] == 1
                        if not enemycheck and not friendlycheck:
                            next_location = list(current_location)
                            if next_location not in self.legal_moves and next_location != self.location:
                                self.legal_moves.append(next_location)
                    except KeyError: #this prevents the pawn from moving past the 4 or last place on the board
                        pass
                for each in (-1, 1): # governs the capturing of pawns
                    current_location = list(self.location)
                    if current_location[1] != size-1:
                        current_location[0] += each
                        current_location[1] += 1
                    elif current_location[1] == size-1:
                        current_location[1] = 0
                        current_location[3] += 1 #this checks for 4-d captures
                        current_location[0] += each
                    try:
                        if self.color == 'white':
                            enemycheck = board[tuple(current_location)] == 2
                            friendlycheck = board[tuple(current_location)] == 1
                        if enemycheck:
                            next_location = list(current_location)
                            if next_location not in self.legal_moves and next_location != self.location:
                                self.legal_moves.append(next_location)
                    except KeyError:
                        pass
            else:
                if self.firstMove == 1:
                    current_location = list(self.location)
                    flag = 0
                    for each in (1,2):
                        current_location[1] =self.location[1]-each
                        try:
                            if self.color == 'black':
                                enemycheck = board[tuple(current_location)] == 1
                                friendlycheck = board[tuple(current_location)] == 2
                            if not enemycheck and not friendlycheck and flag != 1:
                                next_location = list(current_location)
                                if next_location not in self.legal_moves and next_location != self.location:
                                    self.legal_moves.append(next_location)
                            else:
                                flag = 1
                        except KeyError:
                            pass
                for each in (2, 3):
                    current_location = list(self.location)
                    if current_location[each-1] > 0 and each == 2:
                        current_location[each-1] -= 1
                    elif each == 2 and current_location[1] == 0:
                        current_location[3] -= 1
                        current_location[1] = size-1
                    elif each == 3 and current_location[each-1] > 0:
                        current_location[each-1] -= 1
                    try:
                        if self.color == 'black':
                            enemycheck = board[tuple(current_location)] == 1
                            friendlycheck = board[tuple(current_location)] == 2
                        if not enemycheck and not friendlycheck:
                            next_location = list(current_location)
                            if next_location not in self.legal_moves and next_location != self.location:
                                self.legal_moves.append(next_location)
                    except KeyError:
                        pass
                for each in (-1, 1):
                    current_location = list(self.location)
                    if current_location[1] != 0:
                        current_location[0] += each
                        current_location[1] -= 1
                    elif current_location[1] == 0:
                        current_location[1] = size-1
                        current_location[3] -= 1
                        current_location[0] += each
                    try:
                        if self.color == 'black':
                            enemycheck = board[tuple(current_location)] == 1
                            friendlycheck = board[tuple(current_location)] == 2
                        if enemycheck:
                            next_location = list(current_location)
                            if next_location not in self.legal_moves and next_location != self.location:
                                self.legal_moves.append(next_location)
                    except KeyError:
                        pass
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)

        def move(self, location):
            Piece.move(self,location)
            if self.color =='black' and self.location[1]==0 and self.location[3]==0:
                self.promote()
            if self.color =='white' and self.location[1]==size-1 and self.location[3]==size-1:
                self.promote()
        def promote(self):
            location = list(self.location)
            self.take_piece()
            Queen(location,self.color)

    class Rook(Piece):
        def __init__(self, location, color):
            Piece.__init__(self, location, color)
            self.image = 'Rook'

        def find_moves(self, inh=0):
            if inh != 1:
                self.legal_moves = []
            for each in range(0, numberOfDimensions):
                for every in (-1, 1):
                    current_location = list(self.location)
                    flag = 0
                    for all in range(size):
                        if flag == 0:
                            current_location[each] += every
                        try:
                            if self.color == 'white':
                                enemycheck = board[tuple(current_location)] == 2
                            else:
                                enemycheck = board[tuple(current_location)] == 1

                            if (board[tuple(current_location)] == 0 or enemycheck) and flag == 0 and current_location[each ] < size \
                                     and current_location[each] >= 0:

                                next_location = list(current_location)
                                if next_location not in self.legal_moves and next_location != self.location:
                                    self.legal_moves.append(next_location)
                                if enemycheck:
                                    flag = 1
                            else:
                                flag = 1
                        except KeyError:
                            flag = 1

            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)

    classDict = {}
    classDict['Rook'] = Rook
    classDict['Bishop'] = Bishop
    x='Rook'
    y='Bishop'
    classDict['Knight'] = Knight
    classDict['Pawn'] =Pawn
    classDict['ArchBishop'] = ArchBishop
    classDict['Pope'] = Pope
    classDict['NightMare'] = NightMare
    classDict['SpectralSteed'] = SpectralSteed


    class Queen(Piece):

        def __init__(self, location, color):
            Piece.__init__(self, location, color)
            self.image = 'Queen'
            self.inherited = [classDict[x],classDict[y]]

        def find_moves(self, inh=0):
            if inh != 1:
                self.legal_moves = []
            for each in range(0, numberOfDimensions):
                for every in (-1, 1):
                    current_location = list(self.location)
                    flag = 0
                    for all in range(size):
                        if flag == 0:
                            current_location[each] += every
                        try:
                            if self.color == 'white':
                                enemycheck = board[tuple(current_location)] == 2
                            else:
                                enemycheck = board[tuple(current_location)] == 1

                            if (board[tuple(current_location)] == 0 or enemycheck) and flag == 0 and current_location[
                                each] < size \
                                    and current_location[each] >= 0:

                                next_location = list(current_location)
                                if next_location not in self.legal_moves and next_location != self.location:
                                    self.legal_moves.append(next_location)
                                if enemycheck:
                                    flag = 1
                            else:
                                flag = 1
                        except KeyError:
                            flag = 1
            for each in bisCombos:
                for x in (-1,1):
                    for y in (-1,1):
                        flag = 0
                        current_location = list(self.location)
                        for check in (range(size)):
                            if flag == 0:
                                    current_location[each[0]] += x
                                    current_location[each[1]] += y
                                    try:
                                        if self.color == 'white':
                                            enemycheck = board[tuple(current_location)] == 2
                                        else:
                                            enemycheck = board[tuple(current_location)] == 1
                                        boooling = (board[tuple(current_location)] == 0 or enemycheck) and flag == 0 and current_location[each[0]-1] < size and current_location[each[1]-1] < size and current_location[each[0]-1] >= 0 and current_location[each[1]-1] >= 0
                                        if  boooling:
                                            next_location = list(current_location)
                                            if next_location not in self.legal_moves and next_location != self.location:
                                                self.legal_moves.append(next_location)
                                            if enemycheck:
                                                flag = 1
                                        else:
                                            flag = 1
                                    except KeyError:
                                        flag = 1
                            else:
                                pass
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)


    classDict['Queen'] = Queen
    class King(Piece):
        def __init__(self, location,color):
            Piece.__init__(self, location,color)
            self.image = 'King'
        def find_moves(self,inh=0):
            if inh != 1:
                self.legal_moves = []
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    current_location = list(self.location)
                    current_location[0] += x
                    current_location[1] += y
                    if current_location[1] == size:
                        current_location[1] = 0
                        current_location[3] += 1
                    elif current_location[1] == -1:
                        current_location[1] = size-1
                        current_location[3] -= 1
                    try:
                        if self.color == 'white':
                            enemycheck = board[tuple(current_location)] == 2
                        else:
                            enemycheck = board[tuple(current_location)] == 1
                        if (board[tuple(current_location)] == 0 or enemycheck):
                            next_location = list(current_location)
                            if next_location not in self.legal_moves and next_location != self.location:
                                self.legal_moves.append(next_location)
                    except:
                        pass

            for z in (-1, 1):
                current_location = list(self.location)
                current_location[2] += z
                try:
                    if self.color == 'white':
                        enemycheck = board[tuple(current_location)] == 2
                    else:
                        enemycheck = board[tuple(current_location)] == 1
                    if (board[tuple(current_location)] == 0 or enemycheck):
                        next_location = list(current_location)
                        if next_location not in self.legal_moves and next_location != self.location:
                            self.legal_moves.append(next_location)
                except:
                    pass
            if inh != 1:
                for each in self.inherited:
                    each.find_moves(self, 1)
    classDict['King'] = King
def clearBoard():
    global pieceList,pieceDict,bisCombos,ArchBisCombos,popeCombos,KnightCombos,NightmareCombos
    pieceList = []
    pieceDict = {}
    iterarg = []
    for each in range(numberOfDimensions):
        iterarg.append(range(size))
    counter = 0
    for each in itertools.product(*iterarg):
        counter += 1
        board[tuple(each)] = 0
        pieceDict[tuple(each)] = 0
    bisCombos = list(combinations(range(numberOfDimensions), 2))
    ArchBisCombos = list(permutations(range(numberOfDimensions), 3))
    popeCombos = list(permutations(range(numberOfDimensions), 4))
    KnightCombos = list(permutations(range(numberOfDimensions), 2))
    NightmareCombos = list(permutations(range(numberOfDimensions), 3))
    SpectralSteedCombos = list(permutations(range(numberOfDimensions), 4))