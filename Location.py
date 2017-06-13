import TMXLoader

class Location:
    def __init__(self, tmx_path):
        tmx_data = TMXLoader.GetTMX(tmx_path)
        self.tiles = tmx_data.tiles
        self.collisions = tmx_data.collisions
        self.width = tmx_data.total_width
        self.height = tmx_data.total_height
        self.location_above = None
        self.location_to_right = None
        self.location_below = None
        self.location_to_left = None
