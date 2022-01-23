def constrain(t, min, max):
    if t < min:
        t = min
    elif t > max:
        t = max
    return t
class CreateVector2():
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
    def all(self):
        return [self.x, self.y]
    def push(self, forceX, forceY):
        self.x += forceX
        self.y += forceY
    def move(self, x, y):
        self.x = x
        self.y = y
    def collideRect(self, pos1, width1, height1, pos2, width2, height2):
        return pos1.x + width1 > pos2.x and pos1.x < pos2.x + width2 and pos1.y + height1 > pos2.y and pos1.y < pos2.y + height2
    def sub(self, t, optConstrain = 999999):
        return [constrain(self.x - t.x, -optConstrain, optConstrain), constrain(self.y - t.y, -optConstrain, optConstrain)]
