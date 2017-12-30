import zedlib
from player import Player
from location import Location
import pygame


#TODO: Organization
#TODO: Probably a better way to handle interactions
#TODO: Probably a better way to deal with gui

class PlayingState(zedlib.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player(100, 100)
        self.camera = zedlib.Camera(self.game.render_window)
        self.current_location = None
        self.change_location("Field")
        self.set_fps(120)

    def handle_other_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.check_for_npc_interaction()
                elif event.key == pygame.K_e:
                    self.game.change_state(self.game.inventory_state)
                elif event.key == pygame.K_ESCAPE:
                    self.game.change_state(self.game.settings_state)

    def update(self):
        self.player.handle_input()
        self.player.update_movement(self.current_location.collisions)
        self.check_for_passages()
        self.game.gui.update()

    def draw_screen(self):
        self.game.screen.fill((25, 25, 25))
        self.camera.update_target(self.player.rect)
        for tile in self.current_location.tiles:
            self.game.screen.blit(tile.image, self.camera.apply(tile.rect))
        for npc in self.current_location.npcs:
            npc.draw(self.game.screen, self.camera)
        self.player.draw(self.game.screen, self.camera)
        self.game.gui.draw()

    def change_location(self, location_name):
        self.current_location = self.game.get_location(location_name)
        new_width = self.current_location.tmx_data.map_width
        new_height = self.current_location.tmx_data.map_height
        self.camera.update_location_size(new_width, new_height)

    def check_for_passages(self):
        for passage in self.current_location.passages:
            if self.player.rect.colliderect(passage.rect):
                new_passage = self.game.get_passage(passage.passage_to)
                self.change_location(new_passage.location)
                new_passage.update_player_position(self.player)

    def check_for_npc_interaction(self):
        for npc in self.current_location.npcs:
            if self.player.rect.colliderect(npc.rect):
                self.game.dialogue_state.set_messages(npc.messages)
                self.game.dialogue_state.update_name_label(npc.name)
                self.game.change_state(self.game.dialogue_state)
