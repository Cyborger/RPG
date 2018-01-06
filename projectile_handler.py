import math
from projectile import Projectile


class ProjectileHandler:
    def __init__(self, playing_state):
        self.state = playing_state
        self.projectiles = []

    def update_projectiles(self):
        for projectile in self.projectiles:
            self.check_for_collision(projectile)
            
        for projectile in self.projectiles:
            projectile.update_movement()

    def draw_projectiles(self):
        for projectile in self.projectiles:
            projectile.draw(self.state.game.screen, self.state.camera)

    def clear_projectiles(self):
        self.projectiles[:] = []

    def shoot_player_projectile(self):
        mouse_pos = self.state.game.get_mouse_position()
        player_rect = self.state.camera.apply(self.state.player.rect)
        angle = math.atan2(mouse_pos[1] - player_rect.centery,
                           mouse_pos[0] - player_rect.centerx)
        self.projectiles.append(Projectile(self.state.player.rect.centerx,
                                           self.state.player.rect.centery,
                                           angle))

    def check_for_collision(self, projectile):
        for collision in self.state.current_location.collisions:
            if projectile.rect.colliderect(collision.rect):
                self.projectiles.remove(projectile)
                break
