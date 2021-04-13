import sqlite3
import hashlib
import math
import os


class Pokemon:
    def __init__(self, id=1):
        self.ID = id
        self.dfvalues = {
            "name":"bulbasaur",
            "maxxp":1059860,
            "type": {
                1: "Grass",
                2: "Poison"
                    },
            "gender_m":87.5/100,
            "ko":{
                "xp": 64
                },
            "base":{
                "HP": 45, 
                "Attack": 49, 
                "Defense": 49, 
                "Special Attack": 65, 
                "Special Defense": 65, 
                "Speed": 45, 
                "Friend":70
            },
            "MOVS": { #editar
                1: ["MissingMo.1", 10],
                2: ["MissingMo.2", 10],
                3: ["MissingMo.3", 10],
                4: ["MissingMo.4", 10]
                   },
            "description":"",
            "height":"",
            "weight":""
            }
    def GetName(self):
        #pass
        #print("SDA")
        return self.dfvalues["name"]
    def GetMovsBylevel(self, level):
        return self.dfvalues["MOVS"][level]
    def GetRateGender(self):
        return self.dfvalues["gender_m"]
    def GetBaseStats(self):
        return self.dfvalues["base"]["HP"], self.dfvalues["base"]["Attack"], self.dfvalues["base"]["Defense"], self.dfvalues["base"]["Special Attack"], self.dfvalues["base"]["Special Defense"], self.dfvalues["base"]["Speed"]
    def GetKOexp(self):
        return self.dfvalues["ko"]["xp"]
   # def GetKOEvs(self):
   #     return self.dfvalues["ko"]["HP"], self.dfvalues["ko"]["Attack"], self.dfvalues["ko"]["Defense"], self.dfvalues["ko"]["Special Attack"], self.dfvalues["ko"]["Special Defense"], self.dfvalues["ko"]["Speed"]

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



class Pokemon_Player(Pokemon):
    #def __init__(self, id, name, evs, mov, hp, lvl, exp):
    def __init__(self):
        self.pkplayer = {
            "id":1,
            "cname":"lechuga",
            "name":"bulbasaur",
            "level":10,
            "exp":"0",
            "maxxp":1059860,
            "object":"None",
            "type": {
                1: "Grass",
                2: "Poison"
                    },
            "base":{ #Diferente por pokemon
                "HP": 45, 
                "Attack": 49, 
                "Defense": 49, 
                "Special Attack": 65, 
                "Special Defense": 65, 
                "Speed": 45, 
                "Friend":70
            },
            "ivs":{ #Del 0-15 Se genera al capturar un pokemon
                "HP": 45, 
                "Attack": 49, 
                "Defense": 49, 
                "Special": 65, 
                "Speed": 45, 
                "Friend":70
            },
            "evs":{ #65535 max en estadistica, se sube matando pokemons
                "HP": 45, 
                "Attack": 49, 
                "Defense": 49, 
                "Special": 65, 
                "Speed": 45, 
                "Friend":70
            },
            "MOVS": { #editar
                1: ["MissingMo.1", 10],
                2: ["MissingMo.2", 10],
                3: ["MissingMo.3", 10],
                4: ["MissingMo.4", 10]
                   }
            }

    def GetMov(self, id):
        return self.pkplayer["MOVS"][id][0]
    def GetHp(self): #Haha Mateh
        """Get HP of Pokemon"""
        return math.trunc(((((self.pkplayer["base"]["HP"] + self.pkplayer["ivs"]["HP"]) + 50 + (math.sqrt(self.pkplayer["evs"]["HP"])/8)) * self.pkplayer["level"])/50) + 10)

    def GetSAttack(self): #Haha Mateh
        """Get Special Attack of Pokemon"""
        return math.trunc(((((self.pkplayer["base"]["Special Attack"] + self.pkplayer["ivs"]["Special"]) + (math.sqrt(self.pkplayer["evs"]["Special"])/8)) * self.pkplayer["level"])/50) + 5)

    def GetSDefense(self): #Haha Mateh
        """Get Special Defense of Pokemon"""
        return math.trunc(((((self.pkplayer["base"]["Special Defense"] + self.pkplayer["ivs"]["Special"]) + (math.sqrt(self.pkplayer["evs"]["Special"])/8)) * self.pkplayer["level"])/50) + 5)

    def GetSpeed(self): #Haha Mateh
        """Get Speed of Pokemon"""
        return math.trunc(((((self.pkplayer["base"]["Speed"] + self.pkplayer["ivs"]["Speed"]) + (math.sqrt(self.pkplayer["evs"]["Speed"])/8)) * self.pkplayer["level"])/50) + 5)

    def ChangeMovSet(self, id, mov, max):
        """Change Moveset of pokemon with new moviment"""
        self.pkplayer["MOVS"][id] = [mov, max]


    def GetLevelUPNext(self):
        """Get how need for up level"""
        if(self.pkplayer["maxxp"] == 800000): #Fast -100 level
            return (4*pow(self.lvl, 3))/5
        elif(self.pkplayer["maxxp"] == 1000000): #MFast -100 level
            return pow(self.lvl, 3)
        elif(self.pkplayer["maxxp"] == 1059860): #MSlow -100 level
            return (((6/5) * pow(self.lvl, 3)) - (15 * pow(self.pkplayer["level"], 2)) + (100 * self.pkplayer["level"]) - 140)
        elif(self.pkplayer["maxxp"] == 1250000): #Fast -100 level
            return (5*pow(self.lvl, 3))/4

    
    def Action_battle(self, moviemnt):
        print("cut")
    def Action_world(self, moviemnt):
        print("cut")
    def GetMoviments(self):
        print(self.mov)