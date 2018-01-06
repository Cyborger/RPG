import pygame


class Passage:
    def __init__(self, tmx_object, location):
        self.name = tmx_object.name
        self.rect = pygame.Rect(tmx_object.x, tmx_object.y, tmx_object.width,
                                tmx_object.height)
        self.location = location
        self.exit_direction = tmx_object.properties["Exit Direction"]
        self.passage_to = tmx_object.properties["Passage To"]

    def update_player_position(self, player):
        if self.exit_direction == "Up":
            player.position.set_y(self.rect.top - player.rect.height)
            player.position.set_x(self.rect.centerx - player.rect.width/2)
        elif self.exit_direction == "Down":
            player.position.set_y(self.rect.bottom)
            player.position.set_x(self.rect.centerx - player.rect.width/2)
        elif self.exit_direction == "Right":
            player.position.set_y(self.rect.centery - player.rect.height/2)
            player.position.set_x(self.rect.left)
        elif self.exit_direction == "Left":
            player.position.set_y(self.rect.centery - player.rect.height/2)
            player.position.set_x(self.rect.left - player.rect.width)
        player.update_rect_x()
        player.update_rect_y()
