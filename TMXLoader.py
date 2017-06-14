import pytmx
import CollisionObject

class TMXLoader:
    def __init__(self, tmx_path):
        self.tmx_data = pytmx.load_pygame(tmx_path)
        self.tiles = []
        self.objects = []
        self.collisions = []
        self.tile_width = self.tmx_data.tilewidth
        self.tile_height = self.tmx_data.tileheight
        self.tiles_wide = self.tmx_data.width
        self.tiles_high = self.tmx_data.height
        self.total_width = self.tile_width * self.tiles_wide
        self.total_height = self.tile_height * self.tiles_high
        self.locaton_n = self.tmx_data.properties.get("north location")
        self.location_e = self.tmx_data.properties.get("east location")
        self.location_s = self.tmx_data.properties.get("south location")
        self.location_w = self.tmx_data.properties.get("west location")
        self.Load()

    def AddCollision(self, obj):
        new_collision = CollisionObject.CollisionObject(obj.x, obj.y, obj.width,
                                                        obj.height)
        self.objects.append(new_collision)
        self.collisions.append(new_collision)

    def Load(self):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    new_tile = Tile(image, x * self.tile_width,
                                    y * self.tile_height)
                    self.tiles.append(new_tile)

            elif isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    self.AddCollision(obj)

class Tile:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def GetTMXData(file_path):
    tmx_load = TMXLoader(file_path)
    return tmx_load
