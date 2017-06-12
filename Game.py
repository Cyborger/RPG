import pygame
import Player

class Game:
    def __init__(self):
        self.screen_width = 400
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        self.player = Player.Player()

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
        self.player.UpdateMovement()

    def ClearScreen(self):
        self.screen.fill((0, 0, 0))

    def DrawScreen(self):
        self.screen.blit(self.player.image, self.player.rect)

    def UpdateDisplay(self):
        pygame.display.flip()

    def HandleFPS(self):
        self.clock.tick(60)
