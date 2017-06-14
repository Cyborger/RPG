import pygame
import PlayingState

class Game:
    def __init__(self):
        self.screen_width = 30 * 16
        self.screen_height = 30 * 16
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))

        self.playing_state = PlayingState.PlayingState(self)
        self.current_state = self.playing_state
        self.clock = pygame.time.Clock()
        self.running = True

    def GameLoop(self):
        while self.running:
            self.current_state.HandleEvents()
            self.current_state.Update()
            self.current_state.ClearScreen()
            self.current_state.DrawScreen()
            self.current_state.UpdateDisplay()
            self.current_state.HandleFPS()
