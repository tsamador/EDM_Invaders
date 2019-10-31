import pygame
import math
import random
import PlayerShip
import Enemy

# Initialize game engine
pygame.init()

# Define Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) # Color of beat circle
GREEN = (0, 255, 0)     # Color of enemy bullets
RED = (255, 0, 0)       # Color of Enemies
CYAN = (0x01, 0xFF, 0xFF)   # Player ship/bullet color
PI = 3.14159


def main():
    # Time variables
    time = 0  # Used to keep track of bats
    beat = False  # Variable to extend our beat flash longer than 1 frame
    delay = 0

    # Set screen size
    size = (700, 500)
    screen = pygame.display.set_mode(size)

    # display caption
    pygame.display.set_caption("EDM Invaders")

    # Create a font object
    font = pygame.font.Font('Iconsolata', 32);

    # Create a playerShip we will control
    player = PlayerShip.PlayerShip(335, 425, CYAN)

    # Create 10 enemies
    e = []
    enemyx = 100
    for x in range(10):
        e.append(Enemy.Enemy(enemyx, 20, RED, 16))
        enemyx += 60

    done = False

    clock = pygame.time.Clock()

    while not done:

        if time == 120:
            time = 0
        else:
            time += 1

        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys_pressed = pygame.key.get_pressed()
        player.update(keys_pressed, beat)

        #Update each enemy
        for enemy in e:
            enemy.update(beat, player.shots)


        # Screen clearing code
        screen.fill(BLACK)

        # Screen drawing code

        # Draw the player (If they're still alive)
        if player.alive:
            pygame.draw.rect(screen, player.color, player.pos, 2)

        # Calculate if we're 'on' beat
        if time % 30 == 0:
            beat = True
            delay = 1

        if delay > 0:
            delay += 1
            if delay >= 10:
                delay = 0
                beat = False

        pygame.draw.circle(screen, WHITE, [350, 475], 16, 1)
        if delay > 0:
            pygame.draw.circle(screen, WHITE, [350, 475], 15)

        done = True
        for enemy in e:
            if enemy.alive:
                pygame.draw.circle(screen, enemy.color, enemy.pos, 15)
                done = False

        for bullet in player.shots:
            pygame.draw.circle(screen, GREEN, bullet.pos, 2)
        pygame.display.flip()

        clock.tick(60)

    #for x in range(120):

if __name__ == '__main__':
    main()


