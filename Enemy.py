import math
import random
import EnemyBullet

class Enemy:

    enemyShots = []

    def __init__(self,x, y, color, size):
        self.pos = [x, y]
        self.alive = True
        self.direction = -1
        self.color = color
        self.size = size

    # def shoot(self):

    def update(self, beat, bullets):
        if self.alive:
            self.pos[0] = self.pos[0] + 1 * self.direction
            if self.pos[0] < 10:
                self.direction *= -1
                self.pos[1] += 30
            elif self.pos[0] > 660:
                self.direction *= -1
                self.pos[1] += 30
            for b in bullets:
                if math.sqrt((self.pos[0] - b.pos[0]) ** 2 + (self.pos[1] - b.pos[1]) ** 2) <= self.size:
                    self.alive = False
                    b.pos[1] = -1
            # 1% chance for each enemy to shoot every beat
            if random.randint(1, 101) <= 1 and beat:
                self.enemyShots.append(EnemyBullet.EnemyBullet(self.pos[0], self.pos[1], self.color))

    # def updateBullets(self,):