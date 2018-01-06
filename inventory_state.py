import zedlib
import pygame


class InventoryState(zedlib.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.inventory_tile_image = zedlib.load_image("Resources/Images/"\
                                                "InventoryTile.png", scale=4)

        background_image = zedlib.load_image("Resources/Images/"\
                                              "InventoryMenu.png", scale=4)
        self.background = zedlib.Surface(background_image)
        self.background.center_horizontal(self.game.screen.get_rect())
        self.background.center_vertical(self.game.screen.get_rect())

        self.slot_size = self.inventory_tile_image.get_width()
        self.slots_wide = 5
        self.slots_high = 6
        self.spacing = self.slot_size / 4

        scroll_rect_width = (self.slot_size * self.slots_wide
                             + self.spacing * self.slots_wide - 1)
        self.scroll_rect = pygame.Rect(self.background.rect.x + 152,
                                       self.background.rect.y + 20,
                                       scroll_rect_width,
                                       self.background.rect.height - 40)

        self.y_offset = 0
        self.scroll_rate = 50
        self.max_y = (self.slot_size * self.slots_high
                      + self.spacing * self.slots_high - 1)

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.scroll_up()
                elif event.button == 5:
                    self.scroll_down()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_e:
                    self.game.change_state(self.game.playing_state)

    def update(self):
        self.game.gui.update()
    def draw_screen(self):
        self.game.playing_state.draw_screen()
        self.background.draw(self.game.screen)
        self.draw_tiles()

    def draw_tiles(self):
        buffer_surface = pygame.Surface((self.scroll_rect.width, self.max_y),
                                        pygame.SRCALPHA, 32)
        buffer_surface.convert_alpha()
        for y in range(self.slots_high):
            for x in range(self.slots_wide):
                x_pos = x*self.slot_size + x*self.spacing
                y_pos = y*self.slot_size + y*self.spacing
                buffer_surface.blit(self.inventory_tile_image, (x_pos, y_pos))
        crop_rect = pygame.Rect(0, self.y_offset, self.scroll_rect.width,
                                self.scroll_rect.height)
        self.game.screen.blit(buffer_surface.subsurface(crop_rect),
                              self.scroll_rect)


    def scroll_up(self):
        self.y_offset -= self.scroll_rate
        if self.y_offset < 0:
            self.y_offset = 0

    def scroll_down(self):
        self.y_offset += self.scroll_rate
        if self.y_offset > self.max_y - self.scroll_rect.height:
            self.y_offset = self.max_y - self.scroll_rect.height
