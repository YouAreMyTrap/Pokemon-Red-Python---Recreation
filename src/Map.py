import pygame
import os
from Sel_Menu import *
pygame.init()



RESIZE = 2

# Set up the drawing window
# GBA Resolution 240 x 160
screen = pygame.display.set_mode([240 * RESIZE, 160 * RESIZE])     # My eyes hurt with the low res so I scaled up xd
pygame.display.set_caption('Pokemon')

# Game Tick
clock = pygame.time.Clock()

# Img Pallet Town

#Load menu
Menu = Select_Menu(screen, RESIZE)


pallet_town = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'\Levels\pallet_town.png')    # 384 x 365
pallet_town_resized = pygame.transform.scale(pallet_town, (384 * RESIZE, 365 * RESIZE))

posX, posY = 0, 0

def map1(posX, posY):
    screen.blit(pallet_town_resized, (posX, posY))


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


 
        
    # Map movement
    key_down = False
    key_up = False
    key_left = False
    key_right = False

    # Detect Key press
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            posY -= 5  # Move map up = player moves down
            key_down = True
            #print('down')
        if event.key == pygame.K_UP:
            posY += 5  # Move map down = player moves up
            key_up = True
            #print('up')
        if event.key == pygame.K_LEFT:
            posX += 5  # Move map right = player moves left
            key_left = True
            #print('left')
        if event.key == pygame.K_RIGHT:
            posX -= 5  # Move map left = player moves right
            key_right = True
            #print('right')

        # Detect Key release
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            key_down = False
        if event.key == pygame.K_UP:
            key_up = False
            #print("arriba" + str(key_up))
        if event.key == pygame.K_LEFT:
            key_left = False
            #print("left" + str(key_left))
        if event.key == pygame.K_RIGHT:
            key_right = False
            #print("right" + str(key_right))






    # Show map
    screen.fill('black')
    map1(posX, posY)

    # Placeholder player
    circle = pygame.draw.circle(screen, (0, 0, 255), (240, 160), 10)
           #Press menu
   # Menu.KeyBind()  #Si se añade el menu no se puede mover
    # Flip the display
    pygame.display.flip()

    # Update display
    pygame.display.update()
    clock.tick(20)


# Done! Time to quit.

pygame.quit()
