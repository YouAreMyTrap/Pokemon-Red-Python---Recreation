import sys
import os
from settings import *
from sprites import *
from tilemap import *


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

    def load_data(self):
        parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        img_folder = os.path.join(parentDirectory, 'src')
        self.map = Map(os.path.join(parentDirectory, 'maps/map.txt'))
        #parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        ## load map file
        #map_folder = os.path.join(parentDirectory, 'maps')
        #self.map = Map(os.path.abspath(os.path.join(map_folder, 'map.txt')))
        #
        ## load player folder
        #player_folder = os.path.abspath(os.path.join(parentDirectory, 'images/sprite'))
        #
        ## load player sprite
        #Sel_P_Sprite = os.path.abspath(os.path.join(player_folder, 'boy/walk/ss_walk_side.png'))
        #
        #self.spritesheet = Spritesheet(os.path.join(player_folder, PLAYER_SPRITE))


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 10, 10)
        for row, tiles in enumerate(self.map.data): # get all data from map
            for col, tile in enumerate(tiles):
                if tile == "1":                     # all "1" in data file will spawn a wall
                    Wall(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)   # set "camera" for scrolling screen

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Delta Time
            self.events()
            self.update()
            self.draw()

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
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite  in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
