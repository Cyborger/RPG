import pygame
import Player
import Location

class Game:
    def __init__(self):
        self.screen_width = 30 * 16
        self.screen_height = 30 * 16
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        self.player = Player.Player()
        self.starting_location = Location.Location("Resources/TMXMaps/starting_location.tmx")
        self.second_location = Location.Location("Resources/TMXMaps/second_location.tmx")
        self.starting_location.location_to_right = self.second_location
        self.second_location.location_to_left = self.starting_location
        self.current_location = self.starting_location
        self.clock = pygame.time.Clock()
        self.running = True

    def GameLoop(self):
        while self.running:
            self.HandleEvents()
            self.Update()
            self.ClearScreen()
            self.DrawScreen()
            self.UpdateDisplay()
            self.HandleFPS()

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.running = False

    def Update(self):
        self.player.HandleMovementInput()
        self.player.UpdateMovement(self.current_location.collisions)
        self.CheckPlayerOffScreen()

    def ClearScreen(self):
        self.screen.fill((0, 0, 0))

    def DrawScreen(self):
        for tile in self.current_location.tiles:
            self.screen.blit(tile.image, tile.rect)
        self.screen.blit(self.player.image, self.player.rect)

    def UpdateDisplay(self):
        pygame.display.flip()

    def HandleFPS(self):
        self.clock.tick(60)

    def CheckPlayerOffScreen(self):
        if self.player.rect.right > self.current_location.width:
            if self.current_location.location_to_right is not None:
                self.current_location = self.current_location.location_to_right
                self.player.rect.left = 0
            else:
                self.player.rect.right = self.current_location.width
            self.player.UpdateActualPosition()

        elif self.player.rect.left < 0:
            if self.current_location.location_to_left is not None:
                self.current_location = self.current_location.location_to_left
                self.player.rect.right = self.current_location.width
            else:
                self.player.rect.left = 0
            self.player.UpdateActualPosition()
