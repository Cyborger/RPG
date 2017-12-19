import zedlib
import pygame

class NPC(zedlib.GameSprite):
    def __init__(self, tmx_properties, x=0, y=0):
        image = pygame.Surface((30, 30))
        pygame.draw.circle(image, (255, 255, 255), (15, 15), 15)
        super().__init__(image, x, y)
        self.messages = []
        self.load_messages(tmx_properties["Dialogue"])

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
