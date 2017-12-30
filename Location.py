import zedlib
import pygame
from passage import Passage
from npc import NPC


#TODO: Seperate top and bottom layer tiles

class Location:
    def __init__(self, tmx_file_path):
        self.tmx_data = zedlib.load_tmx(tmx_file_path)
        self.name = self.tmx_data.properties["Name"]

        self.tiles = self.load_tiles()
        self.collisions = self.load_collisions() + self.create_boundries()
        self.passages = self.load_passages()
        self.npcs = self.load_npcs()

    def load_tiles(self):
        tile_list = []
        for layer in self.tmx_data.tile_layers:
            for x, y, image in layer.tiles():
                x_pos = x * self.tmx_data.tile_width
                y_pos = y * self.tmx_data.tile_height
                tile_list.append(zedlib.Surface(image, x_pos, y_pos))
        return tile_list

    def load_collisions(self):
        if not self.tmx_data.get_layer("Collisions"): return []

        collision_list = []
        for obj in self.tmx_data.get_layer("Collisions"):
            collision_obj = zedlib.CollisionObject(obj.width, obj.height,
                                                   obj.x, obj.y)
            collision_list.append(collision_obj)
        return collision_list

    def load_passages(self):
        if not self.tmx_data.get_layer("Passages"): return []

        passage_list = []
        for passage in self.tmx_data.get_layer("Passages"):
            passage_list.append(Passage(passage, self.name))
        return passage_list

    def create_boundries(self):
        boundry_list = []
        left = zedlib.CollisionObject(10, self.tmx_data.map_height, -10, 0)
        right = zedlib.CollisionObject(10, self.tmx_data.map_height,
                                       self.tmx_data.map_width, 0)
        top = zedlib.CollisionObject(self.tmx_data.map_width, 10, 0, -10)
        bottom = zedlib.CollisionObject(self.tmx_data.map_width, 10,
                                        0, self.tmx_data.map_height)
        boundry_list.extend([left, right, top, bottom])
        return boundry_list

    def load_npcs(self):
        if not self.tmx_data.get_layer("NPCs"): return []

        npc_list = []
        for npc in self.tmx_data.get_layer("NPCs"):
            npc_list.append(NPC(npc))
        return npc_list
