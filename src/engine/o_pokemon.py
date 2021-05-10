import pygame
import os
from settings import *

from value_player import *

class o_pokemon():
    def __init__(self, screen2, resize, me = 1):
        self.screen = screen2
        self.RESIZE = resize
        self.o2pokemon = False
        self.Player = Player_InGame()
        self.me = me
        self.Menu_Sel = {
            "Poss": 10,
            "Sel": False,
            "Pos2": 0}
        self.pokemons = 1
        
        self.Data = {
                "Img": "ui_" + str(PLAYER_FRAME) + "_",
                "pb": ["open", "close"],
                "pbposs": [[3, 18], [88, 9, 1], [88, 33, 2], [88, 57, 3], [88, 81, 4], [88, 105, 5]],
                "textform":["b_text","b_text2"],
                "text_sel_tx":["Choose POKéMON or CANCEL","Do what with this PKMN?"],
                "arrow pos": [0, [155, 92], [155, 107], [155, 122], [155, 137]],
                "text_sel":["SUMMARY", "CHANGE", "OBJECT", "EXIT"],
                "text_sel_POS":[[162, 90], [162, 105], [162, 120], [162, 135]],
                "options":["DISABLED", 0, 0]
                }


    def Draw(self):
        if self.o2pokemon: self.Print()

    def Load(self):
        """Show/UnShow Menu"""
        self.me = 2
        self.Menu_Sel = {
            "Poss": 10,
            "Sel": False,
            "Pos2": 0}
        self.Data["options"] = ["DISABLED", 0, 0]
        self.o2pokemon = False if self.o2pokemon else True
        

    def Print(self):
        
        pygame.font.init()
        font = pygame.font.Font(parentsource + "\pokemon_fire_red.ttf", 15 * self.RESIZE, bold=True)

        background3 = pygame.image.load(parentsource +"/images/battle_pokemon/b_0.png")    # 384 x 365
        background3_resized = pygame.transform.scale(background3, (240 * self.RESIZE, 160 * self.RESIZE))

       
        b_text = pygame.image.load(parentsource +"/images/battle_pokemon/" + self.Data["textform"][1 if self.Menu_Sel["Sel"] else 0] +".png")
        b_text_resized = pygame.transform.scale(b_text, (240 * self.RESIZE, 160 * self.RESIZE))
            #print(self.Menu_Sel["Poss"])
            
            
        pokeball_exit = pygame.image.load(parentsource +"/images/battle_pokemon/p_" + self.Data["pb"][0 if self.Menu_Sel["Poss"] == 11 else 1] +".png")
        pokeball_exit_resized = pygame.transform.scale(pokeball_exit, (20 * self.RESIZE, 24 * self.RESIZE))

        #pokeball_one  = pygame.image.load(parentsource +"/images/battle_pokemon/p_" + self.Data["pb"][0 if self.Menu_Sel["Poss"] == 10 else 1] +".png")
        #pokeball_one_resized = pygame.transform.scale(pokeball_one, (20 * self.RESIZE, 24 * self.RESIZE))

        self.screen.blit(background3_resized, background3_resized.get_rect())
        self.screen.blit(b_text_resized, b_text_resized.get_rect())
        self.screen.blit(pokeball_exit_resized, (185 * self.RESIZE, 132 * self.RESIZE))

        arrow = pygame.image.load(parentsource +'\images\menu\Arrow.png')    # 6 x 11
        arrow_resized = pygame.transform.scale(arrow, (6 * self.RESIZE, 11 * self.RESIZE))

        self.screen.blit(font.render(self.Data["text_sel_tx"][1 if self.Menu_Sel["Sel"] else 0], False, (72, 72, 72)) ,(10 * self.RESIZE, 135 * self.RESIZE))

        pokeball_player = {} 
        b_sel_resized = {} 
        b_sel = {} 
        pokeball_player_resized = {} 
        for x in self.Player.pokemon:
            b_sel[x] = pygame.image.load(parentsource +"/images/battle_pokemon/b_sel_"+ str(x) + str(1 if (self.Data["options"][1] == x or (self.Data["options"][2] == x and self.Data["options"][0] == "Change")) else 0) +".png")
            b_sel_resized[x] = pygame.transform.scale(b_sel[x], (240 * self.RESIZE, 160 * self.RESIZE))
            
            if self.Player.pokemon[x] == None:
                break
            if x == 1:  
                pokeball_player[x] = pygame.image.load(parentsource +"/images/battle_pokemon/p_" + self.Data["pb"][0 if self.Menu_Sel["Poss"] == 10 else 1] +".png")   
            else:
                pokeball_player[x] = pygame.image.load(parentsource +"/images/battle_pokemon/p_" + self.Data["pb"][0 if self.Menu_Sel["Poss"] == self.Data["pbposs"][x - 1][2] else 1] +".png")

            self.pokemons = x
            pokeball_player_resized[x] = pygame.transform.scale(pokeball_player[x], (20 * self.RESIZE, 24 * self.RESIZE))
            self.screen.blit(b_sel_resized[x], b_sel_resized[x].get_rect())
            self.screen.blit(pokeball_player_resized[x], (self.Data["pbposs"][x - 1][0] * self.RESIZE, self.Data["pbposs"][x - 1][1] * self.RESIZE))



        selb_ui = pygame.image.load(parentsource +'/images/battle_pokemon/'+ self.Data["Img"] + str(self.me) + '.png')    # 240 x 160
        selb_ui_resized = pygame.transform.scale(selb_ui, (240 * self.RESIZE, 160 * self.RESIZE))
        
        if self.Menu_Sel["Sel"]:
            self.screen.blit(selb_ui_resized, selb_ui_resized.get_rect())
            self.screen.blit(arrow_resized, (self.Data["arrow pos"][self.Menu_Sel["Pos2"]][0] * self.RESIZE, self.Data["arrow pos"][self.Menu_Sel["Pos2"]][1] * self.RESIZE))

            self.screen.blit(font.render(self.Data["text_sel"][0], False, (72, 72, 72)) ,(self.Data["text_sel_POS"][0][0] * self.RESIZE, self.Data["text_sel_POS"][0][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data["text_sel"][1], False, (72, 72, 72)) ,(self.Data["text_sel_POS"][1][0] * self.RESIZE, self.Data["text_sel_POS"][1][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data["text_sel"][2], False, (72, 72, 72)) ,(self.Data["text_sel_POS"][2][0] * self.RESIZE, self.Data["text_sel_POS"][2][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data["text_sel"][3], False, (72, 72, 72)) ,(self.Data["text_sel_POS"][3][0] * self.RESIZE, self.Data["text_sel_POS"][3][1] * self.RESIZE))

        pygame.display.flip()

    def UP(self):
        """Move Arrow to DOWN"""
        if not self.Menu_Sel["Sel"]:
            if self.Menu_Sel["Poss"] == 10:
                self.Menu_Sel["Poss"] = 12
                    
            if self.Menu_Sel["Poss"] == 11:
                self.Menu_Sel["Poss"] = self.pokemons
                    
            if self.Menu_Sel["Poss"] == 1:
                self.Menu_Sel["Poss"] = 11
                    
            if self.Menu_Sel["Poss"] > 1:
                self.Menu_Sel["Poss"] -= 1
                
        else:
            if self.Menu_Sel["Pos2"] > 1:
                self.Menu_Sel["Pos2"] -= 1
        
        self.Data["options"][2] = 1 if self.Menu_Sel["Poss"] == 10 else self.Menu_Sel["Poss"] + 1
        #print(self.Data["options"])
            
    def Down(self):
        """Move Arrow to DOWN"""
        if not self.Menu_Sel["Sel"]:
            if self.Menu_Sel["Poss"] == 10:
                self.Menu_Sel["Poss"] = 0
                    
            if self.Menu_Sel["Poss"] == 11:
                self.Menu_Sel["Poss"] = 10

            if self.Menu_Sel["Poss"] == self.pokemons -1:
                self.Menu_Sel["Poss"] = 11

            if self.Menu_Sel["Poss"] < self.pokemons -1:
                self.Menu_Sel["Poss"] += 1
                
        else:
            if self.Menu_Sel["Pos2"] < 4:
                self.Menu_Sel["Pos2"] += 1


        #print(self.Menu_Sel["Poss"])
        self.Data["options"][2] = 1 if self.Menu_Sel["Poss"] == 10 else self.Menu_Sel["Poss"] + 1
        #print(self.Data["options"][2])


    def LEFT(self):
        """Move Arrow to RIGHT"""
        if not self.Menu_Sel["Sel"]:
            self.Menu_Sel["Poss"] = 10
        self.Data["options"][2] = 1
    def RIGHT(self):
        """Move Arrow to RIGHT"""
        if not self.Menu_Sel["Sel"] and not self.Player.pokemon == 1:
            self.Menu_Sel["Poss"] = 1
        elif sself.Player.pokemon == 1:
            self.Menu_Sel["Poss"] = 11
        self.Data["options"][2] = 2

    def Sel(self):

        if self.Menu_Sel["Poss"] == 11:
            if self.Data["options"][0] == "DISABLED": self.Back() 
            else: self.Data["options"] = ["DISABLED",0,0]
            
        elif not self.Menu_Sel["Sel"] and self.Data["options"][0] == "DISABLED":
            self.Menu_Sel["Sel"] = True
            self.Menu_Sel["Pos2"] = 1
        elif self.Data["options"][0] == "DISABLED":
            if self.Menu_Sel["Pos2"] == 2:
                self.Data["options"] = ["Change", 1 if self.Menu_Sel["Poss"] == 10 else self.Menu_Sel["Poss"] + 1, 0]
                self.Menu_Sel["Sel"] = False
                #print(self.Data["options"])
            if self.Menu_Sel["Pos2"] == 4:
                self.Menu_Sel["Sel"] = False
        else:
            #print(self.Menu_Sel["Poss"])
            #print(self.Data["options"][1])
            if self.Data["options"][1] == self.Menu_Sel["Poss"] +1 or (self.Menu_Sel["Poss"] == 10 and self.Data["options"][1] == 1):
                self.Data["options"] = ["DISABLED",0,0]
            else:
                self.Player.ChangePokemon(self.Data["options"][1], self.Data["options"][2])
                self.Data["options"] = ["DISABLED",0,0]

            #print(self.Menu_Sel["Pos2"])
    def Back(self):
        if self.Menu_Sel["Sel"]: 
            self.Menu_Sel["Sel"] = False
        else:
            self.o2pokemon = False