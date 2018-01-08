import zedlib
from playing_state import PlayingState
from dialogue_state import DialogueState
from inventory_state import InventoryState
from settings_state import SettingsState
from location import Location
from gui import GUI
import os


class Game(zedlib.Game):
    def __init__(self):
        super().__init__(1280, 720)
        self.locations = self.load_locations()
        self.gui = GUI(self)

        self.playing_state = PlayingState(self)
        self.dialogue_state = DialogueState(self)
        self.inventory_state = InventoryState(self)
        self.settings_state = SettingsState(self)
        self.change_state(self.playing_state)

    def load_locations(self):
        tmx_directory = "Resources/TMX"
        location_list = []

        for file in os.listdir(tmx_directory):
            if file.endswith(".tmx"):
                print("Loading location: %s" % file)
                path = os.path.join(tmx_directory, file)
                location_list.append(Location(path))
        return location_list

    def get_location(self, location_name):
        for location in self.locations:
            if location.name == location_name:
                return location

    def get_all_passages(self):
        passage_list = []
        for location in self.locations:
            passage_list.extend(location.passages)
        return passage_list

    def get_passage(self, passage_name):
        for passage in self.get_all_passages():
            if passage.name == passage_name:
                return passage
