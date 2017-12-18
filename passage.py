class Passage:
    def __init__(self, name, rect, location, tmx_properties):
        self.name = name
        self.rect = rect
        self.location = location
        self.passage_to = tmx_properties["Passage To"]
        self.exit_direction = tmx_properties["Exit Direction"]

    def update_player_position(self, player):
        if self.exit_direction == "Up":
            player.position.set_y(self.rect.top - player.rect.height - 4)
            player.position.set_x(self.rect.centerx - player.rect.width/2)
        elif self.exit_direction == "Down":
            player.position.set_y(self.rect.bottom + 4)
            player.position.set_x(self.rect.centerx - player.rect.width/2)
        player.update_rect_x()
        player.update_rect_y()
