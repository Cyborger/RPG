import pygame
import math

class Player:
    def __init__(self):
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.actual_x = 0.0
        self.actual_y = 0.0

        self.speed = 4.0
        self.move_x = 0.0
        self.move_y = 0.0


    def HandleMovementInput(self):
        keys_pressed = pygame.key.get_pressed()

        # Horizontal movement
        self.move_x = 0.0
        if keys_pressed[pygame.K_A]:
            self.move_x -= self.speed
        if keys_pressed[pygame.K_D]:
            self.move_x += self.speed

        # Vertical movement
        self.move_y = 0.0
        if keys_pressed[pygame.K_W]:
            self.move_y -= self.speed
        if keys_pressed[pygame.K_S]:
            self.move_y += self.speed

        # Handle diagonal movement
        if self.move_x is not 0.0 and self.move_y is not 0.0:
            self.move_x = (self.speed / math.sqrt(2)) * (self.move_x / self.speed)
            self.move_y = (self.speed / math.sqrt(2)) * (self.move_y / self.speed)

        self.actual_x += self.move_x
        self.actual_y += self.move_y

    def UpdateMovement(self, collisions=[]):
        self.rect.x = int(self.actual_x)
        horizontal_collisions = pygame.sprite.spritecollide(self, collisions,
                                                            False)
        for collision in horizontal_collisions:
            collision.Collide()

        self.rect.y = int(self.actual_y)
        vertical_collisions = pygame.sprite.spritecollide(self, collisions,
                                                          False)
        for collision in vertical_collisions:
            collision.Collide()
