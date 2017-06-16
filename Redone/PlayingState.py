import pygame
import GameState
import Player

class PlayingState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player.Player(50.0, 50.0)
        self.fps = 120

    def GetInput(self):
        self.player.HandleMovementInput()

    def Update(self):
        self.player.UpdateMovement()

    def DrawScreen(self):
        self.game.screen.blit(self.player.image, self.player.rect)
