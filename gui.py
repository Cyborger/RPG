import zedlib


class GUI:
    def __init__(self, game):
        self.game = game
        expand_button_path = "Resources/Buttons/Expand.png"
        compress_button_path = "Resources/Buttons/Compress.png"
        options_button_path = "Resources/Buttons/Options.png"
        inventory_button_path = "Resources/Buttons/Inventory.png"

        self.expand_button = zedlib.Button(expand_button_path, scale=2,
                                           function=self.expand)
        self.compress_button = zedlib.Button(compress_button_path, scale=2,
                                             function=self.compress)
        self.options_button = zedlib.Button(options_button_path, scale=2,
                                            function=self.go_to_settings)
        self.inventory_button = zedlib.Button(inventory_button_path, scale=2,
                                              function=self.go_to_inventory)

        self.options_button.rect.left = self.expand_button.rect.right
        self.inventory_button.rect.left = self.options_button.rect.right
        self.current_buttons = [self.expand_button]

    def update(self):
        for button in self.current_buttons:
            button.update(self.game.get_mouse_position())

    def draw(self):
        for button in self.current_buttons:
            button.draw(self.game.screen)

    def expand(self):
        self.current_buttons = [self.compress_button, self.options_button,
                                self.inventory_button]

    def compress(self):
        self.current_buttons = [self.expand_button]
        self.game.change_state(self.game.playing_state)

    def go_to_inventory(self):
        if self.game.current_state == self.game.inventory_state:
            self.game.change_state(self.game.playing_state)
        else:
            self.game.change_state(self.game.inventory_state)

    def go_to_settings(self):
        if self.game.current_state == self.game.settings_state:
            self.game.change_state(self.game.playing_state)
        else:
            self.game.change_state(self.game.settings_state)
