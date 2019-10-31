class PlayerBullet:

    def __init__(self, x , y, color):
        self.pos = [x, y]
        self.color = color

    def move(self):
        self.pos[1] -= 10

