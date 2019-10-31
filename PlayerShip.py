import PlayerBullet
import pygame


class PlayerShip:

    def __init__(self, x, y, color):
        self.pos = [x, y, 25, 25]
        self.alive = True
        self.color = color
        self.shots = []
        self.delay = 0

    def shoot(self, beat):
        # Can only shoot when we're on beat
        if beat:
            self.shots.append(PlayerBullet.PlayerBullet(self.pos[0] + 13, self.pos[1], self.color))

    def update(self, keys_pressed, beat):
        # First update the ship movement
        if keys_pressed[pygame.K_LEFT]:
            if self.pos[0] > 10:
                self.pos[0] = self.pos[0] - 5

        elif keys_pressed[pygame.K_RIGHT]:
            if self.pos[0] < 660:
                self.pos[0] = self.pos[0] + 5

        if keys_pressed[pygame.K_SPACE] and len(self.shots) <= 1 and self.delay == 0:
            self.shoot(beat)
            self.delay = 1

        # Update delay so we can only fire once per beat.
        if self.delay > 0:
            self.delay += 1
            if self.delay == 10:
                self.delay = 0
        # Now update the bullets
        for bullet in self.shots:
            # move the bullet up
            bullet.move()
            # if we've gone of screen, delete it from the array
            if bullet.pos[1] < -1:
                self.shots.remove(bullet)

