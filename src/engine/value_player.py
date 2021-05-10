from Pokemon import *
#from

#print(Pokemon_Player().GetDamage())
#poke = Pokemon_Player()
#print(poke.GetName())
#r1int(Pokemon_Player())

class PSettings:
    PLAYER_TEXT_SPEED = 1
    PLAYER_BATTLE_SCENE = True
    PLAYER_BATTLE_STYLE = 1
    BATTLE_FIX = False
    PLAYER_SOUND = "MONO"
    PLAYER_BUTTON_MODE = "DISABLED"
    PLAYER_FRAME = 10

class Player_InGame:
    def __init__(self, money=0):
        self.pokemon = {
            1: Pokemon_Battle(),
            2: Pokemon_Battle(),
            3: Pokemon_Battle(),
            4: Pokemon_Battle(),
            5: Pokemon_Battle(),
            6: Pokemon_Battle()
            }
        self.Money = money
        self.Name = "Error"
    def GetStartPokemon(self):
        i = 1
        while i <= 6:
            if not Player_InGame().pokemon[i].GetHealt() == 0:
                return i
            i += 1

    def ChangePokemon(self, pok1, pok2):
        tempok = pok2
        self.pokemon[pok2] = self.pokemon[pok1]
        self.pokemon[pok1] = self.pokemon[tempok]