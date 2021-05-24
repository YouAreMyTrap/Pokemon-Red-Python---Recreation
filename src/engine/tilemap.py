from settings import *
import pytmx


class TiledMap: # Load the tile map data from a tmx file
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = (tm.width * tm.tilewidth)
        self.height = (tm.height * tm.tileheight)
        self.tmxdata = tm

    def render(self, surface): # From the data of the tmx file renders the layers
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self): # Return the size of the map, and render the layer onto the map
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera:
    def __init__(self, width, height): # Create a "Camera" as big as the window size
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity): # Apply the camera to an sprite
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect): # Apply the camera to a rectangle
        return rect.move(self.camera.topleft)

    def update(self, target): # Updates de camera movement of an target
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT /2)

        # Limit scrolling to map size
        x = min(0, x) # left
        y = min(0, y) # top
        x = max(-(self.width - WIDTH), x) # right
        y = max(-(self.height - HEIGHT), y) # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)



