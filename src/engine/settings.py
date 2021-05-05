import pygame as pg
import json
import os
import sys

IMG_EXTENSION = ".png"
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
RESIZE = 2
WIDTH = 240 * RESIZE
HEIGHT = 160 * RESIZE
FPS = 60
TITLE = "Pokemon Python"
BGCOLOR = DARKGREY

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player Settings
PLAYER_TEXT_SPEED = 1
PLAYER_BATTLE_SCENE = True
PLAYER_BATTLE_STYLE = 1
PLAYER_SOUND = "MONO"
PLAYER_BUTTON_MODE = "DISABLED"
PLAYER_FRAME = 10
PLAYER_GENDER = 1 # 0 Boy // 1 Girl

# Path
parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parentsource = os.path.join(parentDirectory, "src")

Path = os.path.normcase('/images/menu/m_')

# Img Folders
img_folder = os.path.join(parentsource, "images")
sprite_folder = os.path.join(img_folder, "sprite")

# Player Sprite
P_GENDER = "b_" if PLAYER_GENDER == 0 else "g_"
s_walk = os.path.join(sprite_folder, (P_GENDER + "walking"))
s_bike = os.path.join(sprite_folder, (P_GENDER + "bike"))
s_pickup = os.path.join(sprite_folder, (P_GENDER + "pickup_sit"))
s_throw = os.path.join(sprite_folder, (P_GENDER + "thr_ball"))
s_particles = os.path.join(sprite_folder, ("particles"))

test = os.path.join(s_walk, (P_GENDER + "walk_front_f1"))
print(test)