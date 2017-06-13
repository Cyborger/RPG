import pygame

class CollisionObject:
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def HorizontalCollide(self, player):
        if player.move_x > 0.0:
            player.rect.right = self.rect.left
        elif player.move_x < 0.0:
            player.rect.left = self.rect.right
        player.UpdateActualXPosition()

    def VerticalCollide(self, player):
        if player.move_y > 0.0:
            player.rect.bottom = self.rect.top
        elif player.move_y < 0.0:
            player.rect.top = self.rect.bottom
        player.UpdateActualYPosition()
