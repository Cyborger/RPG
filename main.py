import Game
import pygame

def play_game():
    pygame.init()
    game = Game.Game()
    game.GameLoop()

if __name__ == "__main__":
    play_game()
