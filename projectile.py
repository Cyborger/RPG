import zedlib
import pygame
import math


class Projectile(zedlib.GameSprite):
    def __init__(self, x, y, angle_radians):
        super().__init__(pygame.Surface((5, 5)), x, y)
        self.image.fill((255, 255, 255))
        self.speed = 6
        self.angle = angle_radians
        self.calculate_velocity()

    def calculate_velocity(self):
        self.x_velocity = math.cos(self.angle) * self.speed
        self.y_velocity = math.sin(self.angle) * self.speed
