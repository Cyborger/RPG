import os
import TMXData

class Location:
    def __init__(self, tmx_path):
        self.tmx = TMXData.TMXData(tmx_path)
        self.width = self.tmx.map_width
        self.height = self.tmx.map_height
        self.tiles = self.tmx.tiles
        self.collisions = self.tmx.collisions

        self.name = self.tmx.GetMapProperty("name")
        self.north_location = self.tmx.GetMapProperty("north_location")
        self.east_location = self.tmx.GetMapProperty("east_location")
        self.south_location = self.tmx.GetMapProperty("south_location")
        self.west_location = self.tmx.GetMapProperty("west_location")

    def GetAdjacentLocation(self, direction):
        location_to_check = None
        if direction == "up":
            location_to_check = self.north_location
        elif direction == "right":
            location_to_check = self.east_location

def GetAllLocations():
    all_locations = []
    for file in os.listdir("Resources/TMXMaps"):
        file_path = os.path.join("Resources/TMXMaps/", file)
        new_location = Location(file_path)
        all_locations.append(new_location)
    return all_locations
