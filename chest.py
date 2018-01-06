import zedlib


class Chest(zedlib.GameSprite):
    def __init__(self, tmx_data):
        spritesheet = zedlib.Spritesheet("Resources/Animations/Chest.png", 2, 1)
        super().__init__(spritesheet.get_first_image(), tmx_data.x, tmx_data.y)
        self.opening_animation = zedlib.Animation(spritesheet.get_all_images(),
                                                  looping=False)
        self.opened = False

    def open(self):
        self.opening_animation.update()
        self.image = self.opening_animation.get_current_frame()
        self.opened = True
