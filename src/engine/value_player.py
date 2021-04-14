from Pokemon import *
#from

print(Pokemon_Player().GetDamage())
#poke = Pokemon_Player()
#print(poke.GetName())
#r1int(Pokemon_Player())

class PSettings:
    PLAYER_TEXT_SPEED = 1
    PLAYER_BATTLE_SCENE = True
    PLAYER_BATTLE_STYLE = 1
    PLAYER_SOUND = "MONO"
    PLAYER_BUTTON_MODE = "DISABLED"
    PLAYER_FRAME = 10

class Player_InGame:
    def __init__(self, money=0):
        self.pokemon = {
            1: Pokemon_Player(),
            2: Pokemon_Player(),
            3: Pokemon_Player(),
            4: Pokemon_Player(),
            5: Pokemon_Player(),
            6: Pokemon_Player()
            }
        self.Money = money
        self.Name = "Error"