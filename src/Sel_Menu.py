import pygame
import os

class Select_Menu:
    def __init__(self, screen2, resize = 0):
        #print("Menu Loaded")
        self.Menu_Loaded = False
        self.screen = screen2
        self.RESIZE = resize
        self.Menu_Sel = 1



    def KeyBind(self): #Continuo el keyimput solucionar
        pressed_keys = pygame.event.wait()
        if (pressed_keys.type == pygame.KEYDOWN) and (pressed_keys.key == pygame.K_o):
            self.Menu_Loaded = False if self.Menu_Loaded else True
        
        if (pressed_keys.type == pygame.KEYDOWN) and (pressed_keys.key == pygame.K_UP):
            self.Menu_Sel -= 1 if not self.Menu_Sel == 1 else 0
        if (pressed_keys.type == pygame.KEYDOWN) and (pressed_keys.key == pygame.K_DOWN):
            self.Menu_Sel += 1 if not self.Menu_Sel == 7 else 0


        if self.Menu_Loaded: self.imprimir()
        
        #print(self.Menu_Sel)
        #if(event.key == pygame.K_o):
        #    print("Press o")
    
    def imprimir(self):
        arrowpos = {
            1: 15,
            2: 45,
            3: 75,
            4: 105,
            5: 135,
            6: 165,
            7: 195
            }
        #Imprime el background
        menu = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'\menu\m_0.png')    # 384 x 365
        menu_resized = pygame.transform.scale(menu, (240 * self.RESIZE, 160 * self.RESIZE))



        arrow = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'\menu\Arrow.png')    # 6 x 11
        arrow_resized = pygame.transform.scale(arrow, (6 * self.RESIZE, 11 * self.RESIZE))


        self.screen.blit(menu_resized, menu_resized.get_rect())
        self.screen.blit(arrow_resized,(350 ,arrowpos[self.Menu_Sel]))

        #Imprime el texto
        pygame.font.init()
        
        font = pygame.font.Font(os.path.dirname(os.path.realpath(__file__)) + "\pokemon_fire_red.ttf", 30, bold=True)
        self.screen.blit(font.render('POKéDEX', False, (96, 96, 96)) ,(370 ,10))
        self.screen.blit(font.render('POKéMON', False, (96, 96, 96)) ,(370 ,40))
        self.screen.blit(font.render('BAG', False, (96, 96, 96)) ,(370 ,70))
        self.screen.blit(font.render('TR ERROR', False, (96, 96, 96)) ,(370 ,100))
        self.screen.blit(font.render('SAVE', False, (96, 96, 96)) ,(370 ,130))
        self.screen.blit(font.render('OPTIONS', False, (96, 96, 96)) ,(370 ,160))
        self.screen.blit(font.render('EXIT', False, (96, 96, 96)) ,(370 ,190))

        #pygame.display.flip()

