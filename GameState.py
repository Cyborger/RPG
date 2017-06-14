import pygame

class GameState:
    def __init__(self, game):
        self.game = game

    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)

    def HandleBasicEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False

    def Update(self):
        pass

    def ClearScreen(self):
        self.game.screen.fill((0, 0, 0))

    def DrawScreen(self):
        pass

    def UpdateDisplay(self):
        pygame.display.flip()

    def HandleFPS(self, fps=60):
        self.game.clock.tick(fps)
