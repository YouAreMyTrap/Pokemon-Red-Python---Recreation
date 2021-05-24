import sqlite3
import hashlib
import math
import random
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
        """Get Mov of level"""
        return self.dfvalues["MOVS"][level]
    def GetRateGender(self):
        """Get Rate Gender"""
        return self.dfvalues["gender_m"]
    def GetBaseStats(self):
        """Get Base Stats"""
        return self.dfvalues["base"]["HP"], self.dfvalues["base"]["Attack"], self.dfvalues["base"]["Defense"], self.dfvalues["base"]["Special Attack"], self.dfvalues["base"]["Special Defense"], self.dfvalues["base"]["Speed"]
    def GetKOexp(self):
        """Get exp when pokemon ko"""
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



class Pokemon_Battle(Pokemon):
    #def __init__(self, id, name, evs, mov, hp, lvl, exp):
    """Pokemon Btalle Object"""
    def __init__(self, name):
        self.pk = {
            "id":1,
            "cname":"lechuga",
            "name":"bulbasaur",
            "level":10,
            "exp":"0",
            "maxxp":1059860,
            "object":"None",
            "healt": 38,
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
            "MOVS": { #editar 1r name 2n pp, 3r maxpp, 4r power
                1: ["MissingMo.1", 19,10,4,"Flying"],
                2: ["-", 32,33,4,"Normal"],
                3: ["-", 11,12,4,"Normal"],
                4: ["-", 42,43,4,"Normal"]
                   }
            }
        self.pk["cname"] = name
    def GetHealt(self):
        """Get current heal of pokemon"""
        return self.pk["healt"]
    def GetLevel(self):
        """Get current level of pokemon"""
        return self.pk["level"]

    def ChangePP(self, mov, action, n = 1):
        """Change PP Value 
            mov = id of mov
            action: rv/sum
            n: number of actions
        """
        if action == "rv":
            self.pk["MOVS"][mov][1] -= n
        elif action == "sum":
            self.pk["MOVS"][mov][1] += n
            
    def RemoveHealt(self, rv):
        """Remove healt of pokemon"""     
        if not self.pk["healt"] <= 0:
            self.pk["healt"] -= int(rv)

        if self.pk["healt"] <= 0:
            self.pk["healt"] = 0
            print("You Kill this pokemon" + self.pk["cname"])

    def GetName(self):
        return (self.pk["cname"], self.pk["name"])
    def GetMov(self, id):
        return self.pk["MOVS"][id]
    def GetHp(self): #Haha Mateh
        """Get HP of Pokemon"""
        return math.trunc(((((self.pk["base"]["HP"] + self.pk["ivs"]["HP"]) + 50 + (math.sqrt(self.pk["evs"]["HP"])/8)) * self.pk["level"])/50) + 10)

    def GetAttack(self):
        """Get Attack of Pokemon"""
        return math.trunc(((((self.pk["base"]["Attack"] + self.pk["ivs"]["Attack"]) + (math.sqrt(self.pk["evs"]["Attack"])/8)) * self.pk["level"])/50) + 5)

    def GetDefense(self): #Haha Mateh
        """Get Defense of Pokemon"""
        return math.trunc(((((self.pk["base"]["Defense"] + self.pk["ivs"]["Defense"]) + (math.sqrt(self.pk["evs"]["Defense"])/8)) * self.pk["level"])/50) + 5)

    def GetSAttack(self): #Haha Mateh
        """Get Special Attack of Pokemon"""
        return math.trunc(((((self.pk["base"]["Special Attack"] + self.pk["ivs"]["Special"]) + (math.sqrt(self.pk["evs"]["Special"])/8)) * self.pk["level"])/50) + 5)

    def GetSDefense(self): #Haha Mateh
        """Get Special Defense of Pokemon"""
        return math.trunc(((((self.pk["base"]["Special Defense"] + self.pk["ivs"]["Special"]) + (math.sqrt(self.pk["evs"]["Special"])/8)) * self.pk["level"])/50) + 5)

    def GetSpeed(self): #Haha Mateh
        """Get Speed of Pokemon"""
        return math.trunc(((((self.pk["base"]["Speed"] + self.pk["ivs"]["Speed"]) + (math.sqrt(self.pk["evs"]["Speed"])/8)) * self.pk["level"])/50) + 5)

    def ChangeMovSet(self, id, mov, max):
        """Change Moveset of pokemon with new moviment"""
        self.pk["MOVS"][id] = [mov, max]

    def GetDamage(self, dmof, enemy): #enemrydef [0]Def [1]SDef
        """Calculate damage and return"""
        #refer link https://bit.ly/34b0iLZ

        return (((2*self.pk["level"]/5 + 2) * self.GetMov(dmof)[3] * self.CalculateA_D(self.GetMov(dmof)[4], [enemy.GetDefense(),enemy.GetSDefense()]))/50 + 2) * self.Calculate_Modifier(self.GetMov(dmof)[4], enemy.pk["type"], ["Water","Fire"])
        pass
    
    def GetLevelUPNext(self):
        """Get how need for up level"""
        if(self.pk["maxxp"] == 800000): #Fast -100 level
            return (4*pow(self.pk["level"], 3))/5
        elif(self.pk["maxxp"] == 1000000): #MFast -100 level
            return pow(self.pk["level"], 3)
        elif(self.pk["maxxp"] == 1059860): #MSlow -100 level
            return (((6/5) * pow(self.pk["level"], 3)) - (15 * pow(self.pk["level"], 2)) + (100 * self.pk["level"]) - 140)
        elif(self.pk["maxxp"] == 1250000): #Fast -100 level
            return (5*pow(self.pk["level"], 3))/4

    def CalculateA_D(self, type, enemydef):
        """Get Value A/D of damage formula"""
        types = {
            "Water": [self.GetSAttack(),1],
            "Grass": [self.GetSAttack(),1],
            "Fire": [self.GetSAttack(),1],
            "Ice": [self.GetSAttack(),1],
            "Electric": [self.GetSAttack(),1],
            "Psychic": [self.GetSAttack(),1],
            "Dragon": [self.GetSAttack(),1],
            "Dark": [self.GetSAttack(),1],
            "Shadow Bolt": [self.GetSAttack(),1],
            "Shadow Chill": [self.GetSAttack(),1],
            "Shadow Fire": [self.GetSAttack(),1],
            "Shadow Rave": [self.GetSAttack(),1],
            "Shadow Storm": [self.GetSAttack(),1],
            "Shadow Wave": [self.GetSAttack(),1],
            
            "Normal": [self.GetAttack(),0],
            "Fighting ": [self.GetAttack(),0],
            "Flying": [self.GetAttack(),0],
            "Ground": [self.GetAttack(),0],
            "Rock": [self.GetAttack(),0],
            "Bug": [self.GetAttack(),0],
            "Ghost": [self.GetAttack(),0],
            "Poison": [self.GetAttack(),0],
            "Steel": [self.GetAttack(),0],
            "Shadow Blast": [self.GetAttack(),0],
            "Shadow Blitz": [self.GetAttack(),0],
            "Shadow Break": [self.GetAttack(),0],
            "Shadow End": [self.GetAttack(),0],
            "Shadow Rush": [self.GetAttack(),0]
        }
        return types[type][0] / enemydef[types[type][1]]

    def Calculate_Modifier(self, mov, etype, stats):
        """Get Value Modifier of damage formula"""
        st = set(stats)
        tplayer = set(self.pk["type"])
        Weather = 1.5 if (("Water" == mov) and ("Rain"in st) or ("Fire" == mov) and ("Harsh sunlight"in st)) else 0.5 if (("Water" == mov) and ("Harsh sunlight"in st) or ("Fire" == mov) and ("Rain"in st)) else 1
        Targets = 0.75
        randoms = random.randint(217,255)/255
        STAB = 1.5 if mov in tplayer else 1  #Atack Bonus
        Type = self.type_effectiveness(mov, etype)
        return Targets * Weather * randoms * STAB * Type

    def  type_effectiveness(self, ptype, etype):
        """Efficiences of pokemon calculator"""
        #refer link https://bit.ly/3fHOlCJ
        types= {
            "Normal":{
                "Rock" : 0.5,
                "Ghost": 0
            },
            "Fire":{
                "Fire" : 0.5,
                "Water": 0.5,
                "Grass": 2,
                "Ice": 2,
                "Bug": 2,
                "Rock": 0.5,
                "Dragon": 0.5
            },
            "Water":{
                "Rock" : 0.5,
                "Ghost": 0
            },
            "Electric":{
                "Water" : 2,
                "Water": 0.5,
                "Grass": 0.5,
                "Ground": 2,
                "Rock": 2,
                "Dragon": 0.5
            },
            "Grass":{
                "Fire" : 0.5,
                "Water": 2,
                "Grass": 0.5,
                "Poison": 0.5,
                "Ground": 2,
                "Flying": 0.5,
                "Bug": 0.5,
                "Rock": 2,
                "Dragon": 0.5
            },
            "Ice":{
                "Water" : 0.5,
                "Grass": 2,
                "Ice": 0.5,
                "Flying": 2,
                "Rock": 2,
                "Dragon": 2
            },
            "Fighting":{
                "Normal" : 2,
                "Ice": 2,
                "Poison": 0.5,
                "Flying": 0.5,
                "Psychic": 0.5,
                "Bug": 0.5,
                "Rock": 2,
                "Ghost": 0
            },
            "Poison":{
                "Grass" : 2,
                "Poison": 0.5,
                "Ground": 0.5,
                "Bug": 2,
                "Rock": 0.5,
                "Ghost": 0.5
            },
            "Ground":{
                "Fire" : 2,
                "Electric": 2,
                "Ground": 0.5,
                "Grass": 0.5,
                "Poison": 2,
                "Flying": 0,
                "Bug": 0.5,
                "Rock": 2
            },
            "Flying":{
                "Electric" : 0.5,
                "Grass": 2,
                "Fighting": 0.5,
                "Bug": 2,
                "Rock": 2
            },
            "Psychic":{
                "Fighting" : 2,
                "Poison": 2,
                "Psychic": 0.5
            },
            "Bug":{
                "Fire" : 0.5,
                "Grass": 2,
                "Fighting": 0.5,
                "Poison": 2,
                "Flying": 0.5,
                "Psychic": 2,
                "Ghost": 0.5
            },
            "Rock":{
                "Fire" : 2,
                "Ice": 2,
                "Fighting": 0.5,
                "Ground": 0.5,
                "Flying": 2,
                "Bug": 2
            },
            "Ghost":{
                "Ghost" : 2
            },
            "Dragon":{
                "Dragon" : 2
            }
        }
        type1 = types[ptype][etype[1]] if etype[1] in types[ptype] else 1
        type2 = types[ptype][etype[2]] if etype[2] in types[ptype] else 1
        return type1 if type1 >= type2 else type2
    def Action_battle(self, moviemnt):
        print("cut")
    def Action_world(self, moviemnt):
        print("cut")
    def GetMoviments(self):
        pass #print(self.mov)

    