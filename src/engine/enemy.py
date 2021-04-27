from Pokemon import *


class Enemy_InGame:
    def __init__(self, money=0):
        self.pokemon = {
            1: Pokemon_Battle(),
            2: Pokemon_Battle(),
            3: Pokemon_Battle(),
            4: Pokemon_Battle(),
            5: Pokemon_Battle(),
            6: Pokemon_Battle()
            }
        self.StartTExt = "Hey Broder"
        self.EndTExt = ["GG", "Fuck You"]
        self.Money = money
        self.Name = "Enemy"