import zedlib
from player import Player
from location import Location
from interaction_handler import InteractionHandler
from projectile_handler import ProjectileHandler
import pygame
import math


#TODO: Organization
#TODO: Probably a better way to deal with gui

class PlayingState(zedlib.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player(100, 100)
        self.camera = zedlib.Camera((self.game.screen_width,
                                     self.game.screen_height))
        self.interaction_handler = InteractionHandler(self)
        self.projectile_handler = ProjectileHandler(self)
        self.current_location = self.change_location("Field")
        self.set_fps(120)

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.interaction_handler.check_for_npc_interaction()
                    self.interaction_handler.check_for_chest_interaction()
                elif event.key == pygame.K_e:
                    self.game.change_state(self.game.inventory_state)
                elif event.key == pygame.K_ESCAPE:
                    self.game.change_state(self.game.settings_state)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.projectile_handler.shoot_player_projectile()

    def handle_input(self):
        self.player.handle_input()

    def update(self):
        self.player.update_movement(self.current_location.collisions)
        self.projectile_handler.update_projectiles()
        self.interaction_handler.check_for_passage_interaction()
        self.game.gui.update()

    def draw_screen(self):
        self.camera.update_target(self.player.rect)
        self.game.screen.fill((25, 25, 25))
        self.current_location.draw_base_layer(self.game.screen, self.camera)
        self.player.draw(self.game.screen, self.camera)
        self.projectile_handler.draw_projectiles()
        self.current_location.draw_top_layer(self.game.screen, self.camera)
        self.game.gui.draw()

    def change_location(self, location_name):
        new_location = self.game.get_location(location_name)
        self.current_location = new_location
        new_width = self.current_location.tmx_data.map_width
        new_height = self.current_location.tmx_data.map_height
        self.camera.update_location_size(new_width, new_height)
        self.projectile_handler.clear_projectiles()
        return new_location
