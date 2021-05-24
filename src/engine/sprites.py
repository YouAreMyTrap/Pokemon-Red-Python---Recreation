from settings import *


class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pg.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, w, h):
        # grab an image out of a larger spritesheet
        sprite = pg.Surface((w, h))
        sprite.blit(self.sprite_sheet,(0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def load_sprites(self):
        self.walk_l = [Spritesheet.parse_sprite(P_GENDER + '_walk_side_f1' + IMG_EXTENSION),
                       Spritesheet.parse_sprite(P_GENDER + '_walk_side_f2' + IMG_EXTENSION),
                       Spritesheet.parse_sprite(P_GENDER + '_walk_side_f3' + IMG_EXTENSION)]
        self.walk_r = []
        for frame in self.walk_l:
            self.walk_r.append(pg.transform.flip(frame, True, False))

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
            print(self.x,self.y)
        if self.collide_with_sign(dx, dy):
            pass #Show message

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                #print("wall")
                return True
        return False

    def collide_with_sign(self, dx=0, dy=0):
        for sign in self.game.interact:
            if sign.x == self.x + dx and sign.y == self.y + dy:
                if sign.x == self.x - dx and sign.y == self.y + dy:
                    if sign.y == self.y + dy:
                        print('sign')
                        return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Sign(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, type):
        self.groups = game.interact
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.type = type

