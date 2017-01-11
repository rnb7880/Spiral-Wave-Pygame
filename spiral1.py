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

excite = pygame.USEREVENT + 1

pygame.time.set_timer(excite, 1000)


coins = [[0 for i in range(10)] for j in range(10)]
for y in range (10):
    for x in range (10):
        coins[y][x] = Coin(x*50 + 10,y*50 + 10)


for line in coins:
    for coin in line:

        for addline in coins:
            for addcoin in addline:
                currx = coin.x
                curry = coin.y
                newx = addcoin.x
                newy = addcoin.y
                if  not (coin.x == addcoin.x and addcoin.y == coin.y):
                    if abs(coin.x - addcoin.x) <= 50 and abs(coin.y - addcoin.y) <= 50:
                        coin.add(addcoin)


while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == excite:
            coins[5][5].excite()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #coins[5][5].chain()
                coins[5][5].excite()
                # print('red')
                # pygame.time.wait(1000)
                # print('wait')
                # coins[5][5].release()
                # print('green')

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
