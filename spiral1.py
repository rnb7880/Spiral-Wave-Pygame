import pygame
import math as m
from spiralClasses import *
GREEN = (0, 255, 0)
RED = (255, 0, 0)

over = False

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SpiralWave")
clock = pygame.time.Clock()

coins = [[0 for i in range(10)] for j in range(10)]
for y in range (10):
    for x in range (10):
        coins[y][x] = Coin(x*50 + 10,y*50 + 10)

for line in coins:
    for coin in line:

        for addline in coins:
            for addcoin in addline:
                if m.fabs(coin.x - addcoin.x) == 1:
                    coin.add(addcoin)


while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                coins[5][5].excite()

    for line in coins:
        for coin in line:
            coin.draw(screen)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
