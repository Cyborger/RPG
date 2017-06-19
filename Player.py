import pygame
import math

import FloatPosition

class Player:
    def __init__(self, start_x=0.0, start_y = 0.0):
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.pos = FloatPosition.FloatPosition(self.rect, start_x, start_y)
        self.pos.UpdateRectPosition()

        self.speed = 2.0
        self.move_x = 0.0
        self.move_y = 0.0

    def HandleMovementInput(self):
        keys_pressed = pygame.key.get_pressed()

        # Horizontal movement
        self.move_x = 0.0
        if keys_pressed[pygame.K_a]:
            self.move_x -= self.speed
        if keys_pressed[pygame.K_d]:
            self.move_x += self.speed

        # Vertical movement
        self.move_y = 0.0
        if keys_pressed[pygame.K_w]:
            self.move_y -= self.speed
        if keys_pressed[pygame.K_s]:
            self.move_y += self.speed

        self.DealWithDiagonalMovement()

        self.pos.x += self.move_x
        self.pos.y += self.move_y

    def DealWithDiagonalMovement(self):
        if self.move_x != 0.0 and self.move_y != 0.0:
            self.move_x = (self.speed / math.sqrt(2.0)) * (self.move_x / self.speed)
            self.move_y = (self.speed / math.sqrt(2.0)) * (self.move_y / self.speed)

    def UpdateMovement(self, collisions=[]):
        self.pos.UpdateRectPositionX()
        horizontal_collisions = pygame.sprite.spritecollide(self, collisions, False)
        for collision_object in horizontal_collisions:
            collision_object.HorizontalCollide(self)

        self.pos.UpdateRectPositionY()
        vertical_collisions = pygame.sprite.spritecollide(self, collisions, False)
        for collision_object in vertical_collisions:
            collision_object.VerticalCollide(self)
