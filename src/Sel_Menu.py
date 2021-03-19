import pygame
import os

class Select_Menu:
    def __init__(self, screen2, resize = 0):
        print("Menu Loaded")
        self.Menu_Loaded = False
        self.screen = screen2
        self.RESIZE = resize



    def KeyBind(self): #Continuo el keyimput solucionar
        pressed_keys = pygame.event.wait()
        if (pressed_keys.type == pygame.KEYDOWN) and (pressed_keys.key == pygame.K_o):
            self.Menu_Loaded = False if self.Menu_Loaded else True
            print(self.Menu_Loaded)
        if self.Menu_Loaded: self.imprimir()

        #if(event.key == pygame.K_o):
        #    print("Press o")
    
    def imprimir(self):

        #Imprime el background
        menu = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'\menu\m_0.png')    # 384 x 365
        menu_resized = pygame.transform.scale(menu, (240 * self.RESIZE, 160 * self.RESIZE))

        self.screen.blit(menu_resized, menu_resized.get_rect())
        

        #Imprime el texto
        pygame.font.init()
        
        font = pygame.font.Font(os.path.dirname(os.path.realpath(__file__)) + "\pokemon_fire_red.ttf", 30, bold=True)
        self.screen.blit(font.render('POKéDEX', False, (0, 0, 0)) ,(370 ,10))
        self.screen.blit(font.render('POKéMON', False, (0, 0, 0)) ,(370 ,40))
        self.screen.blit(font.render('BAG', False, (0, 0, 0)) ,(370 ,70))
        self.screen.blit(font.render('TR ERROR', False, (0, 0, 0)) ,(370 ,100))
        self.screen.blit(font.render('SAVE', False, (0, 0, 0)) ,(370 ,130))
        self.screen.blit(font.render('OPTIONS', False, (0, 0, 0)) ,(370 ,160))
        self.screen.blit(font.render('EXIT', False, (0, 0, 0)) ,(370 ,190))

        #pygame.display.flip()

