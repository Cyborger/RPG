import pygame
import Game

def Main():
    pygame.init()
    game = Game.Game()
    game.RunLoop()

if __name__ == "__main__":
    Main()
