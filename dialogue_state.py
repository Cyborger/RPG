import zedlib
import pygame


class DialogueState(zedlib.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.current_message = None
        text_box_image = zedlib.load_image("Resources/SingleImages/TextBox.png",
                                           4)
        self.text_box = zedlib.Surface(text_box_image, 0, 480)

    def draw_screen(self):
        self.game.playing_state.draw_screen()
        self.game.screen.blit(self.text_box.image, self.text_box.rect)

    def handle_other_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.change_state(self.game.playing_state)
