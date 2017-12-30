import zedlib
import pygame


class NPC(zedlib.GameSprite):
    def __init__(self, tmx_object):
        super().__init__(tmx_object.image, tmx_object.x, tmx_object.y)
        self.name = tmx_object.name
        self.messages = []
        self.load_messages(tmx_object.properties["Dialogue"])

    def load_messages(self, text):
        current_string = text
        while True:
            index = current_string.find("\e")
            if index >0:
                new_message = current_string[:index]
                self.messages.append(new_message)
                current_string = current_string[index + 2:]
            else:
                self.messages.append(current_string)
                break
