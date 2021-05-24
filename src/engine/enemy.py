from Pokemon import *


class Enemy_InGame:
    def __init__(self, money=0):
        self.pokemon = {
            1: Pokemon_Battle("E1"),
            2: Pokemon_Battle("E2"),
            3: Pokemon_Battle("E3"),
            4: Pokemon_Battle("E4"),
            5: Pokemon_Battle("E5"),
            6: Pokemon_Battle("E6")
            }
        self.StartTExt = "Hey Broder"
        self.EndTExt = ["GG", "Fuck You"]
        self.WinMoney = money
        self.LoseMoney = 100
        self.Name = "Enemy"