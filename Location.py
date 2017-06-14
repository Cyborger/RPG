import TMXLoader
import os

class Location:
    def __init__(self, name, tmx_path):
        tmx_data = TMXLoader.GetTMXData(tmx_path)
        self.name = name
        self.tiles = tmx_data.tiles
        self.collisions = tmx_data.collisions
        self.width = tmx_data.total_width
        self.height = tmx_data.total_height
        self.north_location_name = tmx_data.locaton_n
        self.east_location_name = tmx_data.location_e
        self.south_location_name = tmx_data.location_s
        self.west_location_name = tmx_data.location_w

def LoadLocations():
    all_locations = []
    for file in os.listdir("Resources/TMXMaps"):
        file_path = os.path.join("Resources/TMXMaps/", file)
        new_location = Location(file, file_path)
        all_locations.append(new_location)
    return all_locations

def GetLocationByName(string, all_locations):
    for location in all_locations:
        if location.name == string:
            return location
