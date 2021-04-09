import pygame
import os
from settings import *

class Select_Menu:
    def __init__(self, screen2, resize = 0):
        #print("Menu Loaded")
        self.Menu_Loaded = False
        self.screen = screen2
        self.RESIZE = resize
        self.Menu_Sel = 1


    def MenuLoad(self):
        """Show/UnShow Menu"""
        #if self.Menu_Loaded: self.imprimir()
        self.Menu_Loaded = False if self.Menu_Loaded else True
        #print(self.Menu_Loaded)
        
        
    def MenuDown(self):
        """Move Arrow to DOWN"""
        self.Menu_Sel += 1 if not self.Menu_Sel == 7 else 0
    def MenuUP(self):
        """Move Arrow to UP"""
        self.Menu_Sel -= 1 if not self.Menu_Sel == 1 else 0

    def Sel(self):
        """Load menu selection"""
        MenuInput = {
            1: "Pokedex",
            2: "POKéMON",
            3: "BAG",
            4: "TRAINER",
            5: "SAVE",
            6: "OPTIONS",
            7: "EXIT"
            }

        print(MenuInput[self.Menu_Sel])
        if MenuInput[self.Menu_Sel] == "EXIT": self.Menu_Loaded = False
        # def KeyBind(self): #Continuo el keyimput solucionar
            #pressed_keys = pygame.event.wait()
            #if (pressed_keys.type == pygame.KEYDOWN) and (pressed_keys.key == pygame.K_o):
            # self.Menu_Loaded = False if self.Menu_Loaded else True
            
            #if (pressed_keys.type == pygame.KEYDOWN) and (pressed_keys.key == pygame.K_UP):
            #   self.Menu_Sel -= 1 if not self.Menu_Sel == 1 else 0
        


            #if self.Menu_Loaded: self.imprimir()
            
            #print(self.Menu_Sel)
            #if(event.key == pygame.K_o):
            #    print("Press o")
    def Draw(self):
        if self.Menu_Loaded: self.print()


    def Back(self):
        self.Menu_Loaded = False

    def print(self):
        Data = {
            1: [7.5, "A device that records POKéMON secrets", "upon meeting or catching them."],
            2: [22.5, "Check and organize POKéMON that are", "traveling with you in your party."],
            3: [37.5, "Equipped with pockets for storing items", "you bought, received, or found."],
            4: [52.5, "Check your money and other game data.", ""],
            5: [67.5, "Save your game with a complete record", "of your progress to take a break."],
            6: [82.5, "Adjust various game settings such as text", "speed, game rules, etc."],
            7: [97.5, "Close this MENU window,", ""]
            }
        #Imprime el background
        menu = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'\images\menu\m_'+ str(PLAYER_FRAME) +'.png')    # 384 x 365
        menu_resized = pygame.transform.scale(menu, (240 * self.RESIZE, 160 * self.RESIZE))



        arrow = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'\images\menu\Arrow.png')    # 6 x 11
        arrow_resized = pygame.transform.scale(arrow, (6 * self.RESIZE, 11 * self.RESIZE))


        self.screen.blit(menu_resized, menu_resized.get_rect())
        self.screen.blit(arrow_resized,(175 * self.RESIZE, Data[self.Menu_Sel][0] * self.RESIZE))

        #Imprime el texto
        pygame.font.init()
        
        font = pygame.font.Font(os.path.dirname(os.path.realpath(__file__)) + "\pokemon_fire_red.ttf", 15 * self.RESIZE, bold=True)
        self.screen.blit(font.render('POKéDEX', False, (96, 96, 96)) ,(185 * self.RESIZE, 5 * self.RESIZE))
        self.screen.blit(font.render('POKéMON', False, (96, 96, 96)) ,(185 * self.RESIZE, 20 * self.RESIZE))
        self.screen.blit(font.render('BAG', False, (96, 96, 96)) ,(185 * self.RESIZE, 35 * self.RESIZE))
        self.screen.blit(font.render('TR ERROR', False, (96, 96, 96)) ,(185 * self.RESIZE, 50 * self.RESIZE))
        self.screen.blit(font.render('SAVE', False, (96, 96, 96)) ,(185 * self.RESIZE, 65 * self.RESIZE))
        self.screen.blit(font.render('OPTIONS', False, (96, 96, 96)) ,(185 * self.RESIZE, 80 * self.RESIZE))
        self.screen.blit(font.render('EXIT', False, (96, 96, 96)) ,(185 * self.RESIZE, 95 * self.RESIZE))

        self.screen.blit(font.render(Data[self.Menu_Sel][1], False, (255, 255, 255)) ,(5 * self.RESIZE, 125 * self.RESIZE))
        self.screen.blit(font.render(Data[self.Menu_Sel][2], False, (255, 255, 255)) ,(5 * self.RESIZE, 140 * self.RESIZE))

        pygame.display.flip()

