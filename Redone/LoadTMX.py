import pytmx
import CollisionObject

class TMXData:
    def __init__(self, tmx_path):
        self.data = pytmx.load_pygame(tmx_path)
        self.tiles = []
        self.objects = []
        self.collisions = []
        self.tile_width = self.data.tile_width
        self.tile_height = self.data.tile_height
        self.tiles_wide = self.data.width
        self.tiles_high = self.data.height
        self.map_width = self.tile_width * self.tiles_wide
        self.map_height = self.tile_height * self.tiles_high

    def Load(self):
        for layer in self.data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                self.LoadTileLayer(layer)

            elif isinstance(layer, pytmx.TiledObjectGroup):
                self.LoadObjectLayer(layer)

    def LoadTileLayer(self, layer):
        for x, y, image in layer.tiles():
            new_tile = Tile(image, x * self.tile_width, y * self.tile_height)
            self.tiles.append(new_tile)

    def LoadObjectLayer(self, layer):
        for obj in layer:
            self.AddCollision(obj)


    def GetProperty(self, property_name):
        value = self.data.properties.get(property_name)
        return value
