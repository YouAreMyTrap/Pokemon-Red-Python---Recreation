import pygame
import os

class Battle:
    def __init__(self, screen2, resize = 0):
        #print("Menu Loaded")
        self.Menu_Loaded = False
        self.screen = screen2
        self.RESIZE = resize
        self.Menu_Sel = {
            "Poss": 3,
            "Menu": 1
            }


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
            1: [258,247],
            2: [370,247],
            3: [258,280],
            4: [370,280]
            }
        #Imprime el backgrounds
        #background = pygame.image.load("C:/Users\/Pink/Documents/Pokemon-Red-Python---Recreation/Programs/Gba Emu/Pokemon - Edicion Rojo Fuego (Spain)-11.png")
        background = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +"/images/battle/b_0.png")    # 384 x 365
        background_resized = pygame.transform.scale(background, (240 * self.RESIZE, 160 * self.RESIZE))

        #Donde ira el texto
        txt_ui = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'/images/battle/ui_0.png')    # 240 x 160
        txt_ui_resized = pygame.transform.scale(txt_ui, (240 * self.RESIZE, 160 * self.RESIZE))
        
        #Donde el jugador hace las acciones - Menu - Battle
        ui = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'/images/battle/txt_ui_0.png')    # 240 x 160
        ui_resized = pygame.transform.scale(ui, (240 * self.RESIZE, 160 * self.RESIZE))

        arrow = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'/images/battle/Arrow.png')    # 6 x 10
        arrow_resized = pygame.transform.scale(arrow, (6 * self.RESIZE, 10 * self.RESIZE))

        #####Info pokemons#####

        #Enemy
        ienemy = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +"/images/battle/ie_0.png")    # 384 x 365
        ienemy_resized = pygame.transform.scale(ienemy, (240 * self.RESIZE, 160 * self.RESIZE))

        #Player
        iplayer = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +"/images/battle/ip_0.png")    # 384 x 365
        iplayer_resized = pygame.transform.scale(iplayer, (240 * self.RESIZE, 160 * self.RESIZE))


        #####POKEMONS#####
        pknemy = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +"/images/pokemons/caterpie/front.png")    # 384 x 365
        pknemy_resized = pygame.transform.scale(pknemy, (64 * self.RESIZE, 64 * self.RESIZE))

        #Player
        pklayer = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +"/images/pokemons/bulbasaur/back.png")    # 384 x 365
        pklayer_resized = pygame.transform.scale(pklayer, (64 * self.RESIZE, 64 * self.RESIZE))

        self.screen.blit(background_resized, background_resized.get_rect())


        self.screen.blit(pknemy_resized, (290 ,50))
        self.screen.blit(pklayer_resized, (80 ,130))

        self.screen.blit(ui_resized, ui_resized.get_rect())
        self.screen.blit(txt_ui_resized, ui_resized.get_rect())


        self.screen.blit(ienemy_resized, ui_resized.get_rect())
        self.screen.blit(iplayer_resized, ui_resized.get_rect())
        self.screen.blit(arrow_resized, (arrowpos[self.Menu_Sel["Poss"]][0], arrowpos[self.Menu_Sel["Poss"]][1]))

        #Imprime el texto
        pygame.font.init()
        
        font = pygame.font.Font(os.path.dirname(os.path.realpath(__file__)) + "\pokemon_fire_red.ttf", 30, bold=True)
        self.screen.blit(font.render('LUCHA', False, (96, 96, 96)) ,(272 ,242))
        self.screen.blit(font.render('MOCHILA', False, (96, 96, 96)) ,(383 ,242))
        self.screen.blit(font.render('POKéDEX', False, (96, 96, 96)) ,(272 ,275))
        self.screen.blit(font.render('HUIDA', False, (96, 96, 96)) ,(383 ,275))

        pygame.display.flip()

