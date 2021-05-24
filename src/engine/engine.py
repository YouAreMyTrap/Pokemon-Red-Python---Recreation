import sys
import os
from settings import *
from sprites import *
from tilemap import *

from value_player import *
#sys.path.insert(0, os.path.abspath(os.curdir))
from Sel_Menu import *
from battle import *
from o_pokemon import *
from enemy import * 


############# LOAD GAME #############
class Game:
    def __init__(self):
        # Create Window
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.player =  Player_InGame()
        self.Menu = Select_Menu(self.screen ,RESIZE)
        self.o_Pokemon = o_pokemon(self.screen ,RESIZE, self.player)
        self.Battle = Battle(self.screen, self.o_Pokemon, self.player, RESIZE)
        
        

    def load_data(self):
        map_folder = os.path.join(parentsource, 'maps')
        self.map = TiledMap(os.path.join(map_folder, 'palet_town.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(os.path.join(s_walk, (P_GENDER + "walk_front_f1" + IMG_EXTENSION)))



    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.sign = pg.sprite.Group()
        self.bush = pg.sprite.Group()
        self.camera = Camera(self.map.width, self.map.height)  # set "camera" for scrolling screenç
        self.player = Player(self, 10, 58)

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'wall':
                Obstacle(self, (tile_object.x / TILESIZE), (tile_object.y / TILESIZE),
                         tile_object.width, tile_object.height)
            if tile_object.name == 'bush':
                Bush(self, (tile_object.x / TILESIZE), (tile_object.y / TILESIZE),
                         tile_object.width, tile_object.height)
            for signs in signs_tiles:
                if tile_object.name == signs:
                    Sign(self, (tile_object.x / TILESIZE), (tile_object.y / TILESIZE),
                         tile_object.width, tile_object.height)

    def run(self):
        # game loop - set self.playinxxxxxxxxxxg = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Delta Time
            self.update()
            self.draw()
            self.events()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite  in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            
        if not self.o_Pokemon.o2pokemon: self.Menu.Draw()
        if not self.o_Pokemon.o2pokemon: self.Battle.Draw()
        #print(self.o_Pokemon.o2pokemon)
        self.o_Pokemon.Draw()
        pg.display.flip()

    def events(self):
        
        # catch all events here
        for event in pg.event.get(): # z=b x=a a=sel s=op
            if event.type == pg.QUIT: self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: self.quit()

                if event.key == pg.K_s and not self.Battle.Battle:
                    self.Menu.MenuLoad()
                    self.Menu.Menu_Sel = 1
                
                if event.key == pg.K_b and not self.Menu.Menu_Loaded:
                    self.Battle.BattleLoad(Enemy_InGame())
                if self.Menu.Menu_Loaded and not self.o_Pokemon.o2pokemon:
                    if event.key == pg.K_UP: self.Menu.MenuUP()
                    if event.key == pg.K_DOWN: self.Menu.MenuDown()
                    if event.key == pg.K_x: self.Menu.Sel(self.o_Pokemon)
                    if event.key == pg.K_z: self.Menu.Back()
                    #if event.key == pg.K_x: self.Menu.Sel()
                elif self.Battle.Battle and not self.o_Pokemon.o2pokemon:
                    if event.key == pg.K_LEFT: self.Battle.LEFT()
                    if event.key == pg.K_RIGHT: self.Battle.RIGHT()
                    if event.key == pg.K_UP: self.Battle.UP()
                    if event.key == pg.K_DOWN: self.Battle.Down()
                    if event.key == pg.K_x: self.Battle.Sel()
                    if event.key == pg.K_z: self.Battle.Back()
                elif self.o_Pokemon.o2pokemon:
                    if event.key == pg.K_LEFT: self.o_Pokemon.LEFT()
                    if event.key == pg.K_RIGHT: self.o_Pokemon.RIGHT()
                    if event.key == pg.K_UP: self.o_Pokemon.UP()
                    if event.key == pg.K_DOWN: self.o_Pokemon.Down()
                    if event.key == pg.K_x: self.o_Pokemon.Sel(self.Battle)
                    if event.key == pg.K_z: self.o_Pokemon.Back()

                else:
                    #print("SD")
                    if event.key == pg.K_LEFT: self.player.move(dx=-1)
                    if event.key == pg.K_RIGHT: self.player.move(dx=1)
                    if event.key == pg.K_UP: self.player.move(dy=-1)
                    if event.key == pg.K_DOWN: self.player.move(dy=1)   
                    if event.key == pg.K_x: print("Interactuar")
                    


    def show_start_screen(self):
        pass


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
