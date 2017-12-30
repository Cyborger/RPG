import zedlib
import pygame


class SettingsState(zedlib.GameState):
    def __init__(self, game):
        super().__init__(game)
        background_image = zedlib.load_image("Resources/Images/"\
                                             "SettingsMenu.png", scale=4)
        self.background = zedlib.Surface(background_image)
        self.background.center_horizontal(self.game.get_screen_rect())
        self.background.center_vertical(self.game.get_screen_rect())

    def handle_other_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.change_state(self.game.playing_state)

    def update(self):
        self.game.gui.update()
        
    def draw_screen(self):
        self.game.playing_state.draw_screen()
        self.background.draw(self.game.screen)
