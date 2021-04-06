import sqlite3
import hashlib
import math
import os


class Pokemon:
    def __init__(self):
        self.ID = 0
        self.NAME = 0
        self.BaseStats = 0
        self.Mexp = 0
        self.ID = 0
class Pokemon_Pokedex:
    def __init__(self):
        self.ID = 0
        self.NAME = 0
        self.POKEMON_Type_Name = 0
        self.HEIGHT = 0
        self.WEIGHT = 0
        self.DESCRIPCION = 0
        self.TYPE = 0
        self.PAW = 0
        self.AREA = 0
        self.IMAGE_HEIGHT = 0
    def GetPokedex_Pokemon(self, name): 
        """Get info of pokemon selected"""
        return True



class Pokemon_Player:
    #def __init__(self, id, name, evs, mov, hp, lvl, exp):
    def __init__(self, id, name, evs, cname, hp, lvl, exp, object):
        self.id = id
        self.name = name
        self.cname = cname
        self.hp_current = hp
        self.lvl = lvl
        self.exp = exp
        self.exp_max = max_xp
        self.object  = object
        self.BaseStats = {   #Diferente por pokemon
            "HP": 1,
            "Attack": 1,
            "Defense": 1,
            "Special Attack": 1,
            "Special Defense": 1,
            "Speed": 1
                }
        self.evs = { #255 max en estadistica, se sube matando pokemons
            "HP": 1,
            "Attack": 1,
            "Defense": 1,
            "Special Attack": 1,
            "Special Defense": 1,
            "Speed": 1
                }
        self.ivs = {  #Del 0-15 Se genera al capturar un pokemon
            "HP": 1,
            "Attack": 1,
            "Defense": 1,
            "Special Attack": 1,
            "Special Defense": 1,
            "Speed": 1
                }
        self.mov = {
            1: ["MissingMo.1", 10],
            2: ["MissingMo.2", 10],
            3: ["MissingMo.3", 10],
            4: ["MissingMo.4", 10],
        }

    def GetHp(self): #Haha Mateh
        """Get HP of Pokemon"""
        return math.trunc(((((self.BaseStats["HP"] + self.ivs["HP"]) + 50 + (math.sqrt(self.evs["HP"])/8)) * self.lvl)/50) + 10)

    def GetSAttack(self): #Haha Mateh
        """Get Special Attack of Pokemon"""
        return math.trunc(((((self.BaseStats["Special Attack"] + self.ivs["HP"]) + (math.sqrt(self.evs["Special Attack"])/8)) * self.lvl)/50) + 5)

    def GetSDefense(self): #Haha Mateh
        """Get Special Defense of Pokemon"""
        return math.trunc(((((self.BaseStats["Special Defense"] + self.ivs["HP"]) + (math.sqrt(self.evs["Special Defense"])/8)) * self.lvl)/50) + 5)

    def GetSpeed(self): #Haha Mateh
        """Get Speed of Pokemon"""
        return math.trunc(((((self.BaseStats["Speed"] + self.ivs["HP"]) + (math.sqrt(self.evs["Speed"])/8)) * self.lvl)/50) + 5)

    def ChangeMovSet(self, id, mov, max):
        """Change Moveset of pokemon with new moviment"""
        self.mov[id] = ["mov", max]


    def GetLevelUPNext(self):
        """Get how need for up level"""
        if(self.exp_max == 800000): #Fast -100 level
            return (4*pow(self.lvl, 3))/5
        elif(self.exp_max == 1000000): #MFast -100 level
            return pow(self.lvl, 3)
        elif(self.exp_max == 1059860): #MSlow -100 level
            return (((6/5) * pow(self.lvl, 3)) - (15 * pow(self.lvl, 2)) + (100 * self.lvl) - 140)
        elif(self.exp_max == 1250000): #Fast -100 level
            return (5*pow(self.lvl, 3))/4

    
    def Action_battle(self, moviemnt):
        print("cut")
    def Action_world(self, moviemnt):
        print("cut")
    def GetMoviments(self):
        print(self.mov)