import pygame
import os
from settings import *

from value_player import *
from enemy import * 



class Battle:
    def __init__(self, screen2, o_Pokemon, player, resize = 0):
        self.Battle = False
        self.screen = screen2
        self.RESIZE = resize
        self.o_pokemon = o_Pokemon
        self.Player = player
        self.Enemy = Enemy_InGame()
        self.curpokemon = self.Player.GetStartPokemon()
        self.curpokemon2 = 1
        self.pokemons = 1
        self.Menu_Sel = {
            "Poss": 1,
            "Menu": 0,
            }

        self.MenuInput = { #Translate menu position to 1-4
            1: 1,
            2: 2,
            10: 3,
            20: 4
            }
        #Data what need for works, positions, names, images etc in battle menu
        self.Data = {
            0: {
                "Img": "ui_" + str(PLAYER_FRAME),
                1: [129,123.5],
                2: [185,123.5],
                10: [129,140],
                20: [185,140],
                "text1": [136,121,"FIGHT"],
                "text2": [191.5,121,"BAG"],
                "text3": [136,137.5,"POKéMON"],
                "text4": [191.5,137.5,"RUN"],
                "text5": [0,0,""],
                "text6":""},
            1:{
                "Img": "mov_ui_" + str(PLAYER_FRAME),
                1: [9,123.5],
                2: [79,123.5],
                10: [9,140],
                20: [79,140],
                "text1": [16.5,121, str(self.Player.pokemon[self.curpokemon].GetMov(1)[0])],
                "text2": [86,121,str(self.Player.pokemon[self.curpokemon].GetMov(2)[0])],
                "text3": [16.5,137.5,str(self.Player.pokemon[self.curpokemon].GetMov(3)[0])],
                "text4": [86,137.5,str(self.Player.pokemon[self.curpokemon].GetMov(4)[0])],
                "text5": [207,122,str(self.Player.pokemon[self.curpokemon].GetMov(self.GetFixpos())[1])+ "/"+ str(self.Player.pokemon[self.curpokemon].GetMov(self.GetFixpos())[2])],
                "text6": "TYPE/" + str(self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]])[4]).upper()}

        }
        #print(Player_InGame(self.curpokemon).pokemon.GetHp())

    def GetFixpos(self):
        """Fix Position of menu"""
        return self.Menu_Sel["Poss"] if (self.Menu_Sel["Poss"] == 1 or self.Menu_Sel["Poss"] == 2) else 3 if self.Menu_Sel["Poss"] == 10 else 4
    def BattleLoad(self, enemy):
        """New Battle"""
        
        self.Menu_Sel = {
            "Poss": 1,
            "Menu": 0
        }
        self.curpokemon = self.Player.GetStartPokemon()
        print(self.curpokemon)
        self.curpokemon2 = 1

        self.Battle = False if self.Battle else True
        if self.Battle == True: self.Enemy = enemy
        
    def UP(self):
        """Move Arrow to DOWN"""
        self.Menu_Sel["Poss"] = 1 if (self.Menu_Sel["Poss"] == 10 or self.Menu_Sel["Poss"] == 1) else 2

    def Down(self):
        """Move Arrow to DOWN"""
        self.Menu_Sel["Poss"] = 10 if (self.Menu_Sel["Poss"] == 1 or self.Menu_Sel["Poss"] == 10) else 20

    def LEFT(self):
        """Move Arrow to RIGHT"""
        self.Menu_Sel["Poss"] = 1 if (self.Menu_Sel["Poss"] == 2 or self.Menu_Sel["Poss"] == 1) else 10

    def RIGHT(self):
        """Move Arrow to RIGHT"""
        self.Menu_Sel["Poss"] = 2 if (self.Menu_Sel["Poss"] == 1 or self.Menu_Sel["Poss"] == 2) else 20

    def Sel(self):
        """Load menu selection
            0 - Menu Battle Start
            1- Menu Battle Movs
            3 - Menu Pokemons"""
        self.MenuInput = {
            1: ["FIGHT",1, 1, 1],
            2: ["BAG",2, 2, 2],
            3: ["",0,0,3],
            4: ["",0,0,4],
            5: ["",0,0,5],
            6: ["",0,0,6],
            10: ["POKéMON",3, "Bag Error", "Cur pokemo"],
            11: ["",0, "Bag Error", "Exit2"],
            20: ["RUN",4]
            }
            
        print(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])

        print(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])
        
        #Battle
        if isinstance(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], int) and not str(self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[0]) == "-": 
            self.Attack()

        #Menu position
        if self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]] == "FIGHT": 
            self.Menu_Sel["Menu"] = 1
             #print("asd")
        if self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]] == "POKéMON": 
            #self.Menu_Sel["Menu"] = 3
            #self.Menu_Sel["Poss"] = 10
            self.o_pokemon.Load()
            self.o_pokemon.me = 1
        if self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]] == "Exit2": 
            self.Menu_Sel["Menu"] = 0
            self.Menu_Sel["Poss"] = 1
        if self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]] == "RUN": 
            self.Battle = False
            
        
        
    def WhoFirst(self):
       """Select Who pokemon attack first"""
       return  random.choice(["Enemy", "Player"]) if self.Player.pokemon[self.curpokemon].GetSpeed() == self.Enemy.pokemon[self.curpokemon2].GetSpeed() else "Player" if self.Player.pokemon[self.curpokemon].GetSpeed() > self.Enemy.pokemon[self.curpokemon2].GetSpeed() else "Enemy"
        
    def Back(self):
        """Return to Back"""
        if self.Menu_Sel["Menu"] == 1: 
             self.Menu_Sel["Menu"] = 0
        if self.Menu_Sel["Menu"] == 3: 
             self.Menu_Sel["Menu"] = 0  

    def Draw(self):
        """Draw batlle ui if it's loaded"""
        #print(self.Menu_Sel["Poss"] if (self.Menu_Sel["Poss"] == 1 or self.Menu_Sel["Poss"] == 2) else 3 if self.Menu_Sel["Poss"] == 10 else 4)
        if self.Battle: self.__print()

    def IA_sel_move(self):
        """Get what move use enemy"""
        while True:
            rnumber = random.randint(1,4)
            if not self.Enemy.pokemon[self.curpokemon2].pk["MOVS"][rnumber][0] == "-"and not self.Enemy.pokemon[self.curpokemon].GetMov(rnumber)[1] == 0:
                return rnumber

    def Attack(self, change = False):
        """Atack Pokemon"""

        #Verify if no change pokemon
        if not change: damage = self.Player.pokemon[self.curpokemon].GetDamage(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], self.Enemy.pokemon[self.curpokemon2])
                
        #Get enemy atack
        enemy_attack = self.IA_sel_move()
        #Get player atack
        damage2 = self.Enemy.pokemon[self.curpokemon2].GetDamage(enemy_attack, self.Player.pokemon[self.curpokemon])
        if change:
            #if player change pokemon enemy atack (enemy no change pokemons)
            self.Player.pokemon[self.curpokemon].RemoveHealt(damage2)
            self.Enemy.pokemon[self.curpokemon2].ChangePP(enemy_attack, "rv")

        elif self.WhoFirst() == "Player" and not self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1] == 0 and not self.Enemy.pokemon[self.curpokemon2].GetHealt() == 0 and not self.Player.pokemon[self.curpokemon].GetHealt() == 0:     
            #Atack Player to pokemon enemy
            self.Enemy.pokemon[self.curpokemon2].RemoveHealt(damage)
            self.Player.pokemon[self.curpokemon].ChangePP(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], "rv")
                
            if not self.Enemy.pokemon[self.curpokemon2].GetHealt() == 0 and not self.Enemy.pokemon[self.curpokemon2].GetMov(enemy_attack)[1]  == 0:
                #Atack Enemy to pokemon Player
                self.Player.pokemon[self.curpokemon].RemoveHealt(damage2)
                self.Enemy.pokemon[self.curpokemon2].ChangePP(enemy_attack, "rv")

        elif not self.Enemy.pokemon[self.curpokemon].GetMov(enemy_attack)[1] == 0 and not self.Enemy.pokemon[self.curpokemon2].GetHealt() == 0 and not self.Player.pokemon[self.curpokemon].GetHealt() == 0:
            #Atack Enemy to pokemon Player
            self.Player.pokemon[self.curpokemon].RemoveHealt(damage2)
            self.Enemy.pokemon[self.curpokemon2].ChangePP(enemy_attack, "rv")

            if not self.Player.pokemon[self.curpokemon].GetHealt() == 0 and not self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1] == 0:
                #Atack Player to pokemon enemy
                self.Enemy.pokemon[self.curpokemon2].RemoveHealt(damage)
                self.Player.pokemon[self.curpokemon].ChangePP(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], "rv")
        else:
            print("Error No pp or pokemon death")
        #Check pokemon playerhealt it's 0
        if self.Player.pokemon[self.curpokemon].GetHealt() == 0:
            if self.NextPokemon(self.Player) == "Win":
                #Win if player all pokemons death
                print("Win enemy")
                self.Player.Money -= self.Enemy.LoseMoney
                self.Battle = False
            else: 
                #change pokemon automatic if player i have pokemons
                self.curpokemon = self.NextPokemon(self.Player)

        #Check pokemon enemy healt it's 0
        elif self.Enemy.pokemon[self.curpokemon2].GetHealt() == 0:
            if self.NextPokemon(self.Enemy) == "Win":
                #Win if enemy all pokemons death
                print("Win Player")
                self.Player.Money += self.Enemy.WinMoney
                self.Battle = False
            else: 
                #change enemy automatic if player i have pokemons
                self.curpokemon2 = self.NextPokemon(self.Enemy)

        print("""
                Player: %s
                    Healt: %i
                    Max Healt: %i
            
                Enemy: %s
                    Healt: %i
                    Max Healt: %i
        """%(self.Player.pokemon[self.curpokemon].GetName(),self.Player.pokemon[self.curpokemon].GetHealt(),self.Player.pokemon[1].GetHp(),self.Enemy.pokemon[self.curpokemon2].GetName(),self.Enemy.pokemon[self.curpokemon2].GetHealt(),self.Enemy.pokemon[self.curpokemon2].GetHp()))

    def Health_Bar(self, id, max, min):
        pass
    
    def NextPokemon(self, data):
        """Calculate what it's next pokemon"""
        i = 1
        while i <= 6:
            if data.pokemon[i] == None:
                return "Win"
            elif not data.pokemon[i].GetHealt() == 0:
                return i   
            elif data.pokemon[i].GetHealt() == 0 and i == 6:
                return "Win"
            i += 1

    def __print(self):
        """Print on screen"""
        pygame.font.init()
        
        font = pygame.font.Font(parentsource + "\pokemon_fire_red.ttf", 15 * self.RESIZE, bold=True)
        #Imprime el backgrounds
        #background = pygame.image.load("C:/Users\/Pink/Documents/Pokemon-Red-Python---Recreation/Programs/Gba Emu/Pokemon - Edicion Rojo Fuego (Spain)-7.png")
        background = pygame.image.load(parentsource +"/images/battle/b_0.png")    # 384 x 365
        background_resized = pygame.transform.scale(background, (240 * self.RESIZE, 160 * self.RESIZE))

            #Donde ira el texto
            #txt_ui = pygame.image.load(parentsource +'/images/battle/mov_ui_0.png')
        txt_ui = pygame.image.load(parentsource +'/images/battle/'+ self.Data[self.Menu_Sel["Menu"]]["Img"] +'.png')    # 240 x 160
        txt_ui_resized = pygame.transform.scale(txt_ui, (240 * self.RESIZE, 160 * self.RESIZE))
            
            #Donde el jugador hace las acciones - Menu - Battle
            
        ui = pygame.image.load(parentsource +'/images/battle/txt_ui_0.png')    # 240 x 160
        ui_resized = pygame.transform.scale(ui, (240 * self.RESIZE, 160 * self.RESIZE))

        arrow = pygame.image.load(parentsource +'/images/battle/Arrow.png')    # 6 x 10
        arrow_resized = pygame.transform.scale(arrow, (6 * self.RESIZE, 10 * self.RESIZE))

            #####Info pokemons#####

            #Enemy
        ienemy = pygame.image.load(parentsource +"/images/battle/ie_0.png")    # 384 x 365
        ienemy_resized = pygame.transform.scale(ienemy, (240 * self.RESIZE, 160 * self.RESIZE))

            #Player
        iplayer = pygame.image.load(parentsource +"/images/battle/ip_0.png")    # 384 x 365
        iplayer_resized = pygame.transform.scale(iplayer, (240 * self.RESIZE, 160 * self.RESIZE))


            #####POKEMONS#####
        pknemy = pygame.image.load(parentsource +"/images/pokemons/"+ self.Enemy.pokemon[self.curpokemon2].GetName()[1] +"/front.png")    # 384 x 365
        pknemy_resized = pygame.transform.scale(pknemy, (64 * self.RESIZE, 64 * self.RESIZE))

            #Player
        pklayer = pygame.image.load(parentsource +"/images/pokemons/"+ self.Player.pokemon[self.curpokemon].GetName()[1] +"/back.png")    # 384 x 365
        pklayer_resized = pygame.transform.scale(pklayer, (64 * self.RESIZE, 64 * self.RESIZE))

        self.screen.blit(background_resized, background_resized.get_rect())


        self.screen.blit(pknemy_resized, (144 * self.RESIZE, 25 * self.RESIZE))
        self.screen.blit(pklayer_resized, (40  * self.RESIZE, 65 * self.RESIZE))

        self.screen.blit(ui_resized, ui_resized.get_rect())
        self.screen.blit(txt_ui_resized, ui_resized.get_rect())


        self.screen.blit(ienemy_resized, ienemy_resized.get_rect())
        self.screen.blit(iplayer_resized, iplayer_resized.get_rect())
        self.screen.blit(arrow_resized, (self.Data[self.Menu_Sel["Menu"]][self.Menu_Sel["Poss"]][0] * self.RESIZE, self.Data[self.Menu_Sel["Menu"]][self.Menu_Sel["Poss"]][1] * self.RESIZE))

            #Imprime el texto

            #font2 = pygame.font.Font(parentsource + "\pokemon_fire_red.ttf", 15 * self.RESIZE, bold=True)
        
            #Text panel interact
        #print(self.Menu_Sel["Menu"])
        if self.Menu_Sel["Menu"] == 1: 
            self.screen.blit(font.render("TYPE/" + str(self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[4]).upper(), False, (32, 32, 32)) ,(167 * self.RESIZE, 137.5 * self.RESIZE))
            self.screen.blit(font.render(str(self.Player.pokemon[self.curpokemon].GetMov(1)[0]), False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text1"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text1"][1] * self.RESIZE))
            self.screen.blit(font.render(str(self.Player.pokemon[self.curpokemon].GetMov(2)[0]), False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text2"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text2"][1] * self.RESIZE))
            self.screen.blit(font.render(str(self.Player.pokemon[self.curpokemon].GetMov(3)[0]), False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text3"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text3"][1] * self.RESIZE))
            self.screen.blit(font.render(str(self.Player.pokemon[self.curpokemon].GetMov(4)[0]), False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text4"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text4"][1] * self.RESIZE))
            self.screen.blit(font.render(str(self.Player.pokemon[self.curpokemon].GetMov(self.GetFixpos())[1])+ "/"+ str(self.Player.pokemon[self.curpokemon].GetMov(self.GetFixpos())[2]), False, (32, 32, 32)) ,(self.Data[self.Menu_Sel["Menu"]]["text5"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text5"][1] * self.RESIZE))
        else:
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text1"][2], False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text1"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text1"][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text2"][2], False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text2"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text2"][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text3"][2], False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text3"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text3"][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text4"][2], False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text4"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text4"][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text5"][2], False, (32, 32, 32)) ,(self.Data[self.Menu_Sel["Menu"]]["text5"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text5"][1] * self.RESIZE))
                
                
                #Text panel healt
        self.screen.blit(font.render(str(self.Player.pokemon[self.curpokemon].pk["healt"]) + "/ "+ str(self.Player.pokemon[self.curpokemon].GetHp()), False, (32, 32, 32)) ,(193 * self.RESIZE, 94.5 * self.RESIZE))
        self.screen.blit(font.render(self.Player.pokemon[self.curpokemon].pk["cname"], False, (32, 32, 32)) ,(140 * self.RESIZE, 75 * self.RESIZE))
        #self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text6"], False, (32, 32, 32)) ,(167 * self.RESIZE, 137.5 * self.RESIZE))
            
        pygame.display.flip()

