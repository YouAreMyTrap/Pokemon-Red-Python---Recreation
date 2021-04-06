import sqlite3
import hashlib
import math
import os

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
    def __init__(self, id, name, hp, lvl, exp):
        self.id = id
        self.name = name
        self.BaseStats = {
            "HP": 35,
            "Attack": 1,
            "Defense": 1,
            "Special Attack": 1,
            "Special Defense": 1,
            "Speed": 1
                }
        self.evs = {
            "HP": 22850,
            "Attack": 1,
            "Defense": 1,
            "Special Attack": 1,
            "Special Defense": 1,
            "Speed": 1
                }
        self.ivs = {
            "HP": 7,
            "Attack": 1,
            "Defense": 1,
            "Special Attack": 1,
            "Special Defense": 1,
            "Speed": 1
                }
        self.mov = {
            1: "Moviment 1",
            2: "Moviment 2",
            3: "Moviment 3",
            4: "Moviment 4",
        }
        self.hp_current = hp
        self.lvl = lvl
        self.exp = exp

    def GetHp(self): #Haha Mateh
        return math.trunc(((((self.BaseStats["HP"] + self.ivs["HP"]) + 50 + (math.sqrt(self.evs["HP"])/8)) * self.lvl)/50) + 10)

    def GetSAttack(self): #Haha Mateh
        return math.trunc(((((self.BaseStats["Special Attack"] + self.ivs["HP"]) + 50 + (math.sqrt(self.evs["Special Attack"])/8)) * self.lvl)/50) + 5)

    def GetSDefense(self): #Haha Mateh
        return math.trunc(((((self.BaseStats["Special Defense"] + self.ivs["HP"]) + 50 + (math.sqrt(self.evs["Special Defense"])/8)) * self.lvl)/50) + 5)

    def GetSpeed(self): #Haha Mateh
        return math.trunc(((((self.BaseStats["Speed"] + self.ivs["HP"]) + 50 + (math.sqrt(self.evs["Speed"])/8)) * self.lvl)/50) + 5)

    
    def Action_battle(self, moviemnt):
        print("cut")
    def Action_world(self, moviemnt):
        print("cut")
    def GetMoviments(self):
        print(self.mov)