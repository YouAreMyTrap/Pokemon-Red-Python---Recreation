import pygame
import os

class Battle:
    def __init__(self, screen2, resize = 0):
        #print("Menu Loaded")
        self.Menu_Loaded = False
        self.screen = screen2
        self.RESIZE = resize
        self.Menu_Sel = 1


    def MenuLoad(self):
        """Show/UnShow Menu"""
        #print(self.Menu_Loaded)
        if self.Menu_Loaded: self.imprimir()
        self.Menu_Loaded = False if self.Menu_Loaded else True
        
        
    def MenuDown(self):
        """Move Arrow to DOWN"""
        self.Menu_Sel += 1 if not self.Menu_Sel == 7 else 0
    def MenuUP(self):
        """Move Arrow to UP"""
        self.Menu_Sel -= 1 if not self.Menu_Sel == 1 else 0

    def Sel_Menu(self):
        """Load menu selection"""
        MenuInput = {
            1: "Pokedex",
            2: "POKéMON",
            3: "BAG",
            4: "TRAINER"
            }

        print(MenuInput[self.Menu_Sel])
    def imprimir(self):
        arrowpos = {
            1: 15,
            2: 45,
            3: 75,
            4: 105
            }
        #Imprime el backgrounds
        background = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +"/images/battle/b_0.png")    # 384 x 365
        background_resized = pygame.transform.scale(background, (240 * self.RESIZE, 160 * self.RESIZE))



        ui = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'/images/battle/ui_0.png')    # 240 x 160
        ui_resized = pygame.transform.scale(ui, (240 * self.RESIZE, 160 * self.RESIZE))

 
        self.screen.blit(background_resized, background_resized.get_rect())
        self.screen.blit(ui_resized, ui_resized.get_rect())

        #Imprime el texto
       # pygame.font.init()
        
        #font = pygame.font.Font(os.path.dirname(os.path.realpath(__file__)) + "\pokemon_fire_red.ttf", 30, bold=True)
        #self.screen.blit(font.render('POKéDEX', False, (96, 96, 96)) ,(370 ,10))
        #self.screen.blit(font.render('POKéMON', False, (96, 96, 96)) ,(370 ,40))
        #self.screen.blit(font.render('BAG', False, (96, 96, 96)) ,(370 ,70))
        #self.screen.blit(font.render('TR ERROR', False, (96, 96, 96)) ,(370 ,100))
        #self.screen.blit(font.render('SAVE', False, (96, 96, 96)) ,(370 ,130))
        #self.screen.blit(font.render('OPTIONS', False, (96, 96, 96)) ,(370 ,160))
        #self.screen.blit(font.render('EXIT', False, (96, 96, 96)) ,(370 ,190))

        pygame.display.flip()

