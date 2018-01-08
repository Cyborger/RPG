import zedlib
import pygame
from passage import Passage
from npc import NPC
from chest import Chest


#TODO: Seperate top and bottom layer tiles

class Location:
    def __init__(self, tmx_file_path):
        self.tmx_data = zedlib.load_tmx(tmx_file_path)
        self.name = self.tmx_data.properties["Name"]

        self.bottom_layer_tiles, self.top_layer_tiles = self.load_tiles()
        self.collisions = self.load_collisions() + self.create_boundries()
        self.passages = self.load_passages()
        self.npcs = self.load_npcs()
        self.chests = self.load_chests()

    def draw_base_layer(self, screen, camera):
        for obj in self.bottom_layer_tiles + self.npcs + self.chests:
            obj.draw(screen, camera)

    def draw_top_layer(self, screen, camera):
        for tile in self.top_layer_tiles:
            tile.draw(screen, camera)

    def load_tiles(self):
        bottom_layer_tiles, top_layer_tiles = [], []
        for layer in self.tmx_data.tile_layers:
            for x, y, image in layer.tiles():
                x_pos = x * self.tmx_data.tile_width
                y_pos = y * self.tmx_data.tile_height
                tile = zedlib.Surface(image, x_pos, y_pos)
                if "Layer" in layer.properties:
                    if layer.properties["Layer"] == "1":
                        top_layer_tiles.append(tile)
                    else:
                        bottom_layer_tiles.append(tile)
                else:
                    bottom_layer_tiles.append(tile)
        return (bottom_layer_tiles, top_layer_tiles)

    def load_collisions(self):
        if not self.tmx_data.get_layer("Collisions"): return []

        collision_list = []
        for obj in self.tmx_data.get_layer("Collisions"):
            collision_obj = zedlib.CollisionRect(obj.width, obj.height,
                                                   obj.x, obj.y)
            collision_list.append(collision_obj)
        return collision_list

    def load_passages(self):
        if not self.tmx_data.get_layer("Passages"): return []

        passage_list = []
        for passage in self.tmx_data.get_layer("Passages"):
            passage_list.append(Passage(passage, self.name))
        return passage_list

    def load_npcs(self):
        if not self.tmx_data.get_layer("NPCs"): return []

        npc_list = []
        for npc in self.tmx_data.get_layer("NPCs"):
            print("Loading NPC: " + npc.name)
            npc_list.append(NPC(npc))
        return npc_list

    def load_chests(self):
        if not self.tmx_data.get_layer("Chests"): return []

        chest_list = []
        for chest in self.tmx_data.get_layer("Chests"):
            chest_list.append(Chest(chest))
        return chest_list

    def create_boundries(self):
        boundry_list = []
        left = zedlib.CollisionRect(10, self.tmx_data.map_height, -10, 0)
        right = zedlib.CollisionRect(10, self.tmx_data.map_height,
                                       self.tmx_data.map_width, 0)
        top = zedlib.CollisionRect(self.tmx_data.map_width, 10, 0, -10)
        bottom = zedlib.CollisionRect(self.tmx_data.map_width, 10,
                                        0, self.tmx_data.map_height)
        boundry_list.extend([left, right, top, bottom])
        return boundry_list
