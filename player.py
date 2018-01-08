import zedlib
import pygame


class Player(zedlib.GameSprite):
    def __init__(self, x=0, y=0):
        super().__init__(pygame.Surface((24, 24)), x, y)
        self.image.fill((255, 255, 255))
        self.movement_speed = 2.0

    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.move_x += self.movement_speed
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.move_x -= self.movement_speed
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.move_y -= self.movement_speed
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.move_y += self.movement_speed
