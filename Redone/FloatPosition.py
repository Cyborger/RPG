class FloatPosition:
    def __init__(self, rect, x=0.0, y=0.0):
        self.rect = rect
        self.x = x
        self.y = y

    def UpdateFloatPosition(self):
        self.UpdateFloatPositionX()
        self.UpdateFloatPositionY()

    def UpdateFloatPositionX(self):
        self.x = self.rect.x

    def UpdateFloatPositionY(self):
        self.y = self.rect.y

    def UpdateRectPosition(self):
        self.UpdateRectPositionX()
        self.UpdateRectPositionY()

    def UpdateRectPositionX(self):
        self.rect.x = int(self.x)

    def UpdateRectPositionY(self):
        self.rect.y = int(self.y)
