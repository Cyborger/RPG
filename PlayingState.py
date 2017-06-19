import pygame
import GameState
import Player
import Location

class PlayingState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.locations = Location.GetAllLocations()
        self.current_location = self.GetLocationByName("starting_location")
        self.player = Player.Player(32*10.0, 32*10.0)
        self.fps = 120

    def GetInput(self):
        self.player.HandleMovementInput()

    def Update(self):
        self.player.UpdateMovement(self.current_location.collisions)
        self.ManageBoundaries()

    def DrawScreen(self):
        for tile in self.current_location.tiles:
            self.game.screen.blit(tile.image, tile.rect)
        self.game.screen.blit(self.player.image, self.player.rect)

    def ManageBoundaries(self):
        if self.player.rect.right > self.current_location.width:
            if self.current_location.east_location == None:
                self.player.rect.right = self.current_location.width
            else:
                self.ChangeLocation(self.current_location.east_location)
                self.player.rect.left = 0
            self.player.pos.UpdateFloatPositionX()

        elif self.player.rect.left < 0:
            if self.current_location.west_location == None:
                self.player.rect.left = 0
            else:
                self.ChangeLocation(self.current_location.west_location)
                self.player.rect.right = self.current_location.width
            self.player.pos.UpdateFloatPositionX()

        if self.player.rect.bottom > self.current_location.height:
            if self.current_location.south_location == None:
                self.player.rect.bottom = self.current_location.height
            else:
                self.ChangeLocation(self.current_location.south_location)
                self.player.rect.top = 0
            self.player.pos.UpdateFloatPositionY()

        elif self.player.rect.top < 0:
            if self.current_location.north_location == None:
                self.player.rect.top = 0
            else:
                self.ChangeLocation(self.current_location.north_location)
                self.player.rect.bottom = self.current_location.height
            self.player.pos.UpdateFloatPositionY()

    def ChangeLocation(self, new_location):
        self.current_location = self.GetLocationByName(new_location)

    def GetLocationByName(self, string):
        for location in self.locations:
            if location.name == string:
                return location
        print("ERROR: No location found by the name of: " + string)
