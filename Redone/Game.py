import pygame
import PlayingState

class Game:
    def __init__(self):
        self.screen_width = 400
        self.screen_height = 400
        self.screen = pygame.Surface((self.screen_width, self.screen_height))

        self.render_screen_width = self.screen_width
        self.render_screen_height = self.screen_height
        self.render_screen = None
        self.SetResizableWindow()

        self.playing_state = PlayingState.PlayingState(self)
        self.current_state = self.playing_state

        self.clock = pygame.time.Clock()
        self.running = True

    def RunLoop(self):
        while self.running:
            self.current_state.HandleEvents()
            self.current_state.GetInput()
            self.current_state.Update()
            self.current_state.ClearScreen()
            self.current_state.DrawScreen()
            self.current_state.UpdateDisplay()
            self.current_state.HandleFPS()

    def SetResizableWindow(self):
        self.render_screen = pygame.display.set_mode((self.render_screen_width,
                                                      self.render_screen_height),
                                                     pygame.RESIZABLE)

    def SetFullScreenWindow(self):
        self.render_screen = pygame.display.set_mode((self.render_screen_width,
                                                      self.render_screen_height),
                                                     pygame.FULLSCREEN)

    def ResizeWindow(self, new_width, new_height):
        self.render_screen_width = new_width
        self.render_screen_height = new_height
        self.SetResizableWindow()

    def EnterFullscreen(self):
        display_info = pygame.display.Info()
        self.render_screen_width = display_info.current_w
        self.render_screen_height = display_info.current_h
        self.SetFullScreenWindow()
