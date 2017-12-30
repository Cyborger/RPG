import zedlib
import pygame


class DialogueState(zedlib.GameState):
    def __init__(self, game):
        super().__init__(game)
        text_box_image = zedlib.load_image("Resources/Images/TextBox.png",
                                           scale=4)
        self.text_box = zedlib.Surface(text_box_image, 0, 424)

        self.aa = 5

        self.messages = []
        self.message_index = 0
        self.message_label = None
        self.message_rect = pygame.Rect(24, 504, 1232, 200)
        self.message_font = pygame.font.SysFont("Consolas", 24)

        self.name_label = None
        self.name_rect = pygame.Rect(64, 444, 300, 28)
        self.name_font = pygame.font.SysFont("Arial", 25)

    def draw_screen(self):
        self.game.playing_state.draw_screen()
        self.text_box.draw(self.game.screen)
        self.message_label.draw(self.game.screen)
        self.name_label.draw(self.game.screen)

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
            self.update_message_label()

    def set_messages(self, messages):
        self.messages = messages[:]
        self.current_message = self.messages[0]
        self.update_message_label()

    def clear_messages(self):
        self.message_index = 0
        self.messages[:] = []

    def update_message_label(self):
        current_message = self.messages[self.message_index]
        new_label = zedlib.TextLabel(current_message, self.message_rect,
                                     self.message_font, aa=self.aa)
        self.message_label = new_label

    def update_name_label(self, name):
        self.name_label = zedlib.TextLabel(name, self.name_rect, self.name_font,
                                           aa = self.aa)
