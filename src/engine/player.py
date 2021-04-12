from Pokemon import *
#from


print(Pokemon(1).GetKOEvs())

class PSettings:
    PLAYER_TEXT_SPEED = 1
    PLAYER_BATTLE_SCENE = True
    PLAYER_BATTLE_STYLE = 1
    PLAYER_SOUND = "MONO"
    PLAYER_BUTTON_MODE = "DISABLED"
    PLAYER_FRAME = 10

class Player:
    def __init__(self):
        #self.pokemon = Pokemon_Player()
        self.Money = 0
        self.Name = "Error"