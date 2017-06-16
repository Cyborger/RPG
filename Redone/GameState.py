import pygame

class GameState:
    def __init__(self, game):
        self.game = game
        self.fps = 60

    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)

    def GetInput(self):
        pass

    def Update(self):
        pass

    def ClearScreen(self):
        self.game.screen.fill((0, 0, 0))

    def DrawScreen(self):
        pass

    def UpdateDisplay(self):
        rendered_surface = pygame.transform.scale(self.game.screen,
                                                  (self.game.render_screen_width,
                                                   self.game.render_screen_height))
        self.game.render_screen.blit(rendered_surface, (0, 0))
        pygame.display.flip()

    def HandleFPS(self):
        self.game.clock.tick(self.fps)

    def HandleBasicEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.game.ResizeWindow(event.w, event.h)
