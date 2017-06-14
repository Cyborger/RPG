import GameState
import Player
import Location

class PlayingState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player.Player()
        self.all_locations = Location.LoadLocations()
        self.current_location = Location.GetLocationByName("starting location.tmx", self.all_locations)

    def Update(self):
        self.player.HandleMovementInput()
        self.player.UpdateMovement(self.current_location.collisions)
        self.CheckPlayerOffScreen()

    def DrawScreen(self):
        for tile in self.current_location.tiles:
            self.game.screen.blit(tile.image, tile.rect)

        self.game.screen.blit(self.player.image, self.player.rect)

    def CheckPlayerOffScreen(self):
        north_loc = Location.GetLocationByName(self.current_location.north_location_name)
        east_loc = Location.GetLocationByName(self.current_location.east_location_name)
        south_loc = Location.GetLocationByName(self.current_location.south_location_name)
        west_loc = Location.GetLocationByName(self.current_location.west_location_name)

        if self.player.rect.right > self.current_location.width:
            if east_loc is None:
                self.player.rect.right = self.current_location.width
            else:
                self.current_location = east_loc
                self.player.rect.left = 0
            self.player.UpdateActualXPosition()

        if self.player.rect.left < 0:
            if west_loc is None:
                self.player.rect.left = 0
            else:
                self.current_location = west_loc
                self.player.rect.right = self.current_location.width
            self.player.UpdateActualXPosition()

        if self.player.rect.top < 0:
            if north_loc is None:
                self.player.rect.top = 0
            else:
                self.current_location = north_loc
                self.player.rect.bottom = self.current_location.height
            self.player.UpdateActualYPosition()

        if self.player.rect.bottom > self.current_location.height:
            if south_loc is None:
                self.player.rect.bottom = self.current_location.height
            else:
                self.current_location = south_loc
                self.player.top = 0
            self.player.UpdateActualYPosition()

    def GetLocation(self, location_name):
        for location in self.all_locations:
            if location.name == location_name:
                return location
