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

EXCITE = pygame.USEREVENT + 1

rad = 5
many = 20


coins = [[0 for i in range(many)] for j in range(many)]
for y in range (many):
    for x in range (many):
        coins[y][x] = Coin(x*5*rad + rad,y*5*rad + rad,rad)

toexcite = []
excited = []


for line in coins:
    for coin in line:

        for addline in coins:
            for addcoin in addline:
                currx = coin.x
                curry = coin.y
                newx = addcoin.x
                newy = addcoin.y
                if  not (coin.x == addcoin.x and addcoin.y == coin.y):
                    if abs(coin.x - addcoin.x) <= 5*rad and abs(coin.y - addcoin.y) <= 5*rad:
                        coin.add(addcoin)


while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('hit space')
                coins[1][1].excite()
            if event.key == pygame.K_RETURN:
                for line in coins:
                    for coin in line:
                        if coin.color == (255,0,0):
                            for adj in coin.adjacent:
                                if adj not in excited:
                                    toexcite.append(adj)
                        coin.release()
                        coin.draw(screen)
                for coin in toexcite:
                    coin.excite()
                excited = toexcite
                toexcite = []


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
