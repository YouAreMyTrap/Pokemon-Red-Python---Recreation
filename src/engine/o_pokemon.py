import pygame
import os
from settings import *


class o_pokemon():
    def __init__(self, screen2, resize, player, me = 1,):
        self.screen = screen2
        self.RESIZE = resize
        self.o2pokemon = False
        self.Player = player
        self.curpokemon = self.Player.GetStartPokemon()
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
                "arrow pos": {
                    1:[0, [155, 107], [155, 122], [155, 137], [155, 137]],
                    2: [0, [155, 92], [155, 107], [155, 122], [155, 137]],
                    3: [0, [155, 107], [155, 122], [155, 137], [0, 0]],
                    4: [0, [155, 122], [155, 137], [0, 0], [0, 0]]
                    },
                "text_sel":{
                    1:["", "CHANGE", "SUMMARY", "EXIT"],
                    2:["SUMMARY", "CHANGE", "OBJECT", "EXIT"],
                    3:["", "SUMMARY", "OBJECT", "EXIT"],
                    4:["", "", "SUMMARY", "EXIT"]},
                "text_sel_POS":[[162, 90], [162, 105], [162, 120], [162, 135]],
                "options":["DISABLED", 0, 0],
                "pokename_pos":[[30,30], [115,10], [115,35], [115,60], [115,83], [115,106]],
                "pokelvl_pos":[[35,42], [125,20], [125,45], [125,70], [125,93], [125,116]],
                "pokehp_pos":[[56,62], [210,20], [210,45], [210,70], [210,93], [210,116]]
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

        b_sel = {} 
        pokemon_player = {} 
        pokeball_player = {} 
        b_sel_resized = {} 
        pokemon_player_resized = {} 
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


            #print(self.Player.pokemon[x].GetName()[1])
            pokemon_player[x]  = pygame.image.load(parentsource +"/images/pokemons/" + str(self.Player.pokemon[x].GetName()[1]) +"/icon.gif")  

            self.pokemons = x
            pokeball_player_resized[x] = pygame.transform.scale(pokeball_player[x], (20 * self.RESIZE, 24 * self.RESIZE))
            pokemon_player_resized[x] = pygame.transform.scale(pokemon_player[x], (32 * self.RESIZE, 32 * self.RESIZE))
            self.screen.blit(b_sel_resized[x], b_sel_resized[x].get_rect())
            self.screen.blit(pokeball_player_resized[x], (self.Data["pbposs"][x - 1][0] * self.RESIZE, self.Data["pbposs"][x - 1][1] * self.RESIZE))
            self.screen.blit(pokemon_player_resized[x], (self.Data["pbposs"][x - 1][0] * self.RESIZE - 10, self.Data["pbposs"][x - 1][1] * self.RESIZE - 10 ))

            self.screen.blit(font.render(self.Player.pokemon[x].GetName()[0], False, (248, 248, 248)) ,(self.Data["pokename_pos"][x -1][0] * self.RESIZE, self.Data["pokename_pos"][x -1][1] * self.RESIZE))
            self.screen.blit(font.render("Nv" + str(self.Player.pokemon[x].GetLevel()), False, (248, 248, 248)) ,(self.Data["pokelvl_pos"][x -1][0] * self.RESIZE, self.Data["pokelvl_pos"][x -1][1] * self.RESIZE))
            self.screen.blit(font.render(str(self.Player.pokemon[x].GetHealt()) + "/" + str(self.Player.pokemon[x].GetHp()), False, (248, 248, 248)) ,(self.Data["pokehp_pos"][x -1][0] * self.RESIZE, self.Data["pokehp_pos"][x -1][1] * self.RESIZE))



        selb_ui = pygame.image.load(parentsource +'/images/battle_pokemon/'+ self.Data["Img"] + str(2 if self.me == 2 and not self.pokemons == 1 else 12 if self.me == 2 and self.pokemons == 1 else 1 if self.pokemons == 1 else 12) + '.png')    # 240 x 160
        selb_ui_resized = pygame.transform.scale(selb_ui, (240 * self.RESIZE, 160 * self.RESIZE))
        if self.Menu_Sel["Sel"]:
            self.screen.blit(selb_ui_resized, selb_ui_resized.get_rect())
            self.screen.blit(arrow_resized, (self.Data["arrow pos"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][self.Menu_Sel["Pos2"]][0] * self.RESIZE, self.Data["arrow pos"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][self.Menu_Sel["Pos2"]][1] * self.RESIZE))

            self.screen.blit(font.render(self.Data["text_sel"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][0], False, (72, 72, 72)) ,(self.Data["text_sel_POS"][0][0] * self.RESIZE, self.Data["text_sel_POS"][0][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data["text_sel"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][1], False, (72, 72, 72)) ,(self.Data["text_sel_POS"][1][0] * self.RESIZE, self.Data["text_sel_POS"][1][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data["text_sel"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][2], False, (72, 72, 72)) ,(self.Data["text_sel_POS"][2][0] * self.RESIZE, self.Data["text_sel_POS"][2][1] * self.RESIZE))
            self.screen.blit(font.render(self.Data["text_sel"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][3], False, (72, 72, 72)) ,(self.Data["text_sel_POS"][3][0] * self.RESIZE, self.Data["text_sel_POS"][3][1] * self.RESIZE))
        
        self.screen.blit(font.render("Exit", False, (248, 248, 248)) ,(210 * self.RESIZE, 137 * self.RESIZE))
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
            if (self.Menu_Sel["Pos2"] < 4 and self.me == 2 and not self.pokemons == 1) or (self.Menu_Sel["Pos2"] < 3 and self.me == 2 and self.pokemons == 1) or (self.Menu_Sel["Pos2"] < 3 and self.me == 1  and not self.pokemons == 1) or (self.Menu_Sel["Pos2"] < 2 and self.me == 1  and self.pokemons == 1):
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
        if not self.Menu_Sel["Sel"] and not self.pokemons == 1:
            self.Menu_Sel["Poss"] = 1
        elif self.pokemons == 1:
            self.Menu_Sel["Poss"] = 11
        self.Data["options"][2] = 2

    def Sel(self, battle):
        #problema en el ultimo [] - solo funciona con el 1r y he necesito que vaya con los demas menus
        var = self.Menu_Sel["Pos2"] -1 if self.me == 2 and not self.pokemons == 1 else self.Menu_Sel["Pos2"] if self.me == 1 and not self.pokemons == 1 else self.Menu_Sel["Pos2"] + 0 if self.me == 2 and self.pokemons == 1 else self.Menu_Sel["Pos2"] + 1
        print(self.Data["text_sel"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][var])
        #print(self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4)
        #print(var)
        if self.Menu_Sel["Poss"] == 11: self.Back() 
        elif not self.Menu_Sel["Sel"] and self.Data["options"][0] == "DISABLED":
            self.Menu_Sel["Sel"] = True
            self.Menu_Sel["Pos2"] = 1
        elif self.Data["options"][0] == "DISABLED":
            if self.Data["text_sel"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][var] == "CHANGE":
                if self.me == 2:
                    self.Data["options"] = ["Change", 1 if self.Menu_Sel["Poss"] == 10 else self.Menu_Sel["Poss"] + 1, 0]
                    self.Menu_Sel["Sel"] = False
                else:
                    battle.curpokemon = 2
                    self.o2pokemon = False
                    #self.Back()
                    battle.Attack(True)
                    print("change")
            if self.Data["text_sel"][self.me if not self.pokemons == 1 else 3 if self.me == 2 else 4][var] == "EXIT":
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
        if self.Data["options"][0] == "DISABLED":
            if self.Menu_Sel["Sel"]: 
                self.Menu_Sel["Sel"] = False
                print("w")
            else:
                self.o2pokemon = False
                print("E")
        else: self.Data["options"] = ["DISABLED",0,0]