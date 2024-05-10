import random as rand
class Game:
    def __init__(self, id):
        self.turn = "white"
        self.p_data = ["waiting", "waiting"]
        self.last_move = []
        self.id = id
        self.p1name = "0" #unused will be used when Menu is added,
        self.p2name = "1"
        self.gameRules = []
        self.started = False
    def update_turn(self):
        if self.turn == "white":
            self.turn = "black"
        elif self.turn == "black":
            self.turn = "white"
    def decideRules(self):
        masterlist = []
        list0 =  self.gameRules[0]
        list1 = self.gameRules[1]
        for i, (each, every) in enumerate(zip(list0,list1)):
            masterlist.append(rand.choice((each,every)))
        self.gameRules = masterlist

