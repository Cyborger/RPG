import zedlib
import pygame


class DialogueState(zedlib.GameState):
    def __init__(self, game):
        super().__init__(game)
        text_box_image = zedlib.load_image("Resources/SingleImages/TextBox.png",
                                           4)
        self.text_box = zedlib.Surface(text_box_image, 0, 480)

        self.messages = []
        self.message_index = 0
        self.current_message = None
        self.current_message_label = None

        self.dialogue_rect = pygame.Rect(20, 500, 1240, 200)
        self.aa = 5
        font_size = 24
        self.font = pygame.font.SysFont("Consolas", font_size)

    def draw_screen(self):
        self.game.playing_state.draw_screen()
        self.game.screen.blit(self.text_box.image, self.text_box.rect)
        self.game.screen.blit(self.current_message_label.image,
                              self.current_message_label.rect)

    def handle_other_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_message()

    def next_message(self):
        self.message_index += 1
        if self.message_index + 1 > len(self.messages):
            self.clear_messages()
            self.game.change_state(self.game.playing_state)
        else:
            self.current_message = self.messages[self.message_index]
            self.create_dialogue_text()

    def set_messages(self, messages):
        self.messages = messages[:]
        self.current_message = self.messages[0]
        self.create_dialogue_text()

    def clear_messages(self):
        self.message_index = 0
        self.messages[:] = []

    def create_dialogue_text(self):
        new_label = zedlib.TextLabel(self.current_message, self.dialogue_rect,
                                     self.font, aa=self.aa)
        self.current_message_label = new_label
