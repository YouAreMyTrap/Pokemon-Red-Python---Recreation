import pygame
import os
from settings import *

from value_player import *
from enemy import * 



class Battle:
    def __init__(self, screen2, o_Pokemon, resize = 0):
        #print("Menu Loaded")
        self.Battle = False
        self.screen = screen2
        self.RESIZE = resize
        self.o_pokemon = o_Pokemon
        self.Player = Player_InGame()
        self.Enemy = Enemy_InGame()
        self.curpokemon = self.Player.GetStartPokemon()
        self.curpokemon2 = 1
        self.pokemons = 1
        self.Menu_Sel = {
            "Poss": 1,
            "Menu": 0,
            }

        self.MenuInput = {
            1: 1,
            2: 2,
            10: 3,
            20: 4
            }
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
        return self.Menu_Sel["Poss"] if (self.Menu_Sel["Poss"] == 1 or self.Menu_Sel["Poss"] == 2) else 3 if self.Menu_Sel["Poss"] == 10 else 4
    def BattleLoad(self):
        """Show/UnShow Menu"""
        self.Battle = False if self.Battle else True
        
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
            
        #print(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])


        if isinstance(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], int) and not str(self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[0]) == "-": 
            #print(self.Player.pokemon[1].GetHealt())
            #print(self.WhoFirst())




            damage = self.Player.pokemon[1].GetDamage(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], self.Enemy.pokemon[self.curpokemon2])
                
            #CREAR IA QUE ELIJA QUE MOVIMIENTOS VA MEJOR, AHORA SOLO SELECIONA EL MISMO QUE EL JUGADOR
            damage2 = self.Enemy.pokemon[1].GetDamage(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], self.Player.pokemon[self.curpokemon])
            
            if self.WhoFirst() == "Player" and not self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1] == 0 and not self.Enemy.pokemon[self.curpokemon2].GetHealt() == 0 and not self.Player.pokemon[self.curpokemon].GetHealt() == 0:
                
                self.Enemy.pokemon[self.curpokemon2].RemoveHealt(damage)
                self.Player.pokemon[self.curpokemon].ChangePP(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], "rv")

                #print(self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1])
                
                if not self.Enemy.pokemon[self.curpokemon2].GetHealt() == 0 and not self.Enemy.pokemon[self.curpokemon2].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1]  == 0:
                    #print("2")
                    self.Player.pokemon[self.curpokemon].RemoveHealt(damage2)
                    self.Enemy.pokemon[self.curpokemon2].ChangePP(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], "rv")
                    #print(self.Player.Enemy[self.curpokemon2].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1])

            elif not self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1] == 0  and not self.Enemy.pokemon[self.curpokemon2].GetHealt() == 0 and not self.Player.pokemon[self.curpokemon].GetHealt() == 0:
                self.Player.pokemon[self.curpokemon].RemoveHealt(damage2)
                self.Enemy.pokemon[self.curpokemon2].ChangePP(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], "rv")
                #print(self.Player.Enemy[self.curpokemon2].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1])

                if not self.Player.pokemon[self.curpokemon].GetHealt() == 0 and not self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1] == 0:
                    #print("3")
                    self.Enemy.pokemon[self.curpokemon2].RemoveHealt(damage)
                    self.Player.pokemon[self.curpokemon].ChangePP(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]], "rv")
                   # print(self.Player.pokemon[self.curpokemon].GetMov(self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])[1])
            else:
                print("No pp")
                print("No hp")

           
           
            #print(self.Enemy.pokemon[1])
            
            #print(damage)
            print("""
                Player: %s
                    Healt: %i
                    Max Healt: %i
            
                Enemy: %s
                    Healt: %i
                    Max Healt: %i
            
            """%(self.Player.pokemon[1].GetName(),self.Player.pokemon[1].GetHealt(),self.Player.pokemon[1].GetHp(),self.Enemy.pokemon[1].GetName(),self.Enemy.pokemon[1].GetHealt(),self.Enemy.pokemon[1].GetHp()))
            #self.Player.GetStartPokemon()
            #print(self.Player.pokemon[1].GetDamage((self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]])))


        if self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]] == "FIGHT": 
             self.Menu_Sel["Menu"] = 1
             #print("asd")
        if self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]] == "POKéMON": 
             self.Menu_Sel["Menu"] = 3
             self.Menu_Sel["Poss"] = 10
        if self.MenuInput[self.Menu_Sel["Poss"]][self.Menu_Sel["Menu"]] == "Exit2": 
             self.Menu_Sel["Menu"] = 0
             self.Menu_Sel["Poss"] = 1
        
        
    def WhoFirst(self):
       """Select Who pokemon attack first"""
       return  random.choice(["Enemy", "Player"]) if self.Player.pokemon[self.curpokemon].GetSpeed() == self.Enemy.pokemon[self.curpokemon2].GetSpeed() else "Player" if self.Player.pokemon[self.curpokemon].GetSpeed() > self.Enemy.pokemon[self.curpokemon2].GetSpeed() else "Enemy"
        
    def Back(self):
        if self.Menu_Sel["Menu"] == 1: 
             self.Menu_Sel["Menu"] = 0
        if self.Menu_Sel["Menu"] == 3: 
             self.Menu_Sel["Menu"] = 0  

    def Draw(self):
        #print(self.Menu_Sel["Poss"] if (self.Menu_Sel["Poss"] == 1 or self.Menu_Sel["Poss"] == 2) else 3 if self.Menu_Sel["Poss"] == 10 else 4)
        if self.Battle: self.print()


    def Health_Bar(self, id, max, min):
        pass

    def print(self):
        pygame.font.init()
        
        font = pygame.font.Font(parentsource + "\pokemon_fire_red.ttf", 15 * self.RESIZE, bold=True)
        #Imprime el backgrounds
        #background = pygame.image.load("C:/Users\/Pink/Documents/Pokemon-Red-Python---Recreation/Programs/Gba Emu/Pokemon - Edicion Rojo Fuego (Spain)-7.png")
        if self.Menu_Sel["Menu"] == 0 or self.Menu_Sel["Menu"] == 1:
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
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text1"][2], False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text1"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text1"][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text2"][2], False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text2"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text2"][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text3"][2], False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text3"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text3"][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text4"][2], False, (72, 72, 72)) ,(self.Data[self.Menu_Sel["Menu"]]["text4"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text4"][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text5"][2], False, (32, 32, 32)) ,(self.Data[self.Menu_Sel["Menu"]]["text5"][0] * self.RESIZE,self.Data[self.Menu_Sel["Menu"]]["text5"][1] * self.RESIZE))
            
            
            #Text panel healt
            self.screen.blit(font.render(str(self.Player.pokemon[self.curpokemon].pk["healt"]) + "/ "+ str(self.Player.pokemon[self.curpokemon].GetHp()), False, (32, 32, 32)) ,(193 * self.RESIZE, 94.5 * self.RESIZE))
            self.screen.blit(font.render(self.Player.pokemon[self.curpokemon].pk["cname"], False, (32, 32, 32)) ,(140 * self.RESIZE, 75 * self.RESIZE))
            #print("asd")
            self.screen.blit(font.render(self.Data[self.Menu_Sel["Menu"]]["text6"], False, (32, 32, 32)) ,(167 * self.RESIZE, 137.5 * self.RESIZE))
            
        if self.Menu_Sel["Menu"] == 3:
            self.o_pokemon().load()
        
        pygame.display.flip()

