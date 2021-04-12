import pygame as pg
import json
import os
import sys

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
RESIZE = 3
WIDTH = 240 * RESIZE   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 160 * RESIZE  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Pokemon Python"
BGCOLOR = DARKGREY

TILESIZE = 8 * RESIZE
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPRITE = "boy/walk/ss_walk_side.png"

PLAYER_TEXT_SPEED = 1
PLAYER_BATTLE_SCENE = True
PLAYER_BATTLE_STYLE = 1
PLAYER_SOUND = "MONO"
PLAYER_BUTTON_MODE = "DISABLED"
PLAYER_FRAME = 10

parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
#parentsource = os.path.abspath(os.path.join(os.getcwd()))
parentsource = os.path.join(parentDirectory, "src")