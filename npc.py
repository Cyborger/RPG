import zedlib
import pygame

class NPC(zedlib.GameSprite):
    def __init__(self, tmx_properties, x=0, y=0):
        image = pygame.Surface((30, 30))
        pygame.draw.circle(image, (255, 255, 255), (15, 15), 15)
        super().__init__(image, x, y)
