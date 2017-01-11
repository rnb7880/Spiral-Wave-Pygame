import pygame
import math as m
from spiralClasses import *

"""
General Pygame Setup
"""
over = False
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SpiralWave")
clock = pygame.time.Clock()
GO = pygame.USEREVENT + 1


"""
Board Customization
"""
rad = 3
many = 10
COLOR1 = (0, 0, 0)
COLOR2 = (0, 0, 255)

"""
Creation of board
"""
coins = [[0 for i in range(many)] for j in range(many)]
for y in range (many):
    for x in range (many):
        coins[y][x] = Coin(x*5*rad + rad,y*5*rad + rad,rad,COLOR1,COLOR2)
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


"""
Starting conditions
"""
starty = 2
startx = 2
num_start = 2
speed = 999 #milliseconds


"""
WERK WERK WERK
"""
pygame.time.set_timer(GO,speed)
starters = []
null = []
toexcite = []
excitedold = []
excitednew = []
for i in range(num_start):
    starters.append(coins[startx+i][starty])
    null.append(coins[startx+i][starty+1])
null.append(coins[startx-1][starty+1])
null.append(coins[startx-1][starty])
null.append(coins[startx+num_start][starty+1])
null.append(coins[startx+num_start][starty])

print(null)

while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('hit space')
                excited = null
                for i in range(len(starters)):
                    starters[i].excite()
                    excited.append(starters[i])
                null = []


#Uncomment and comment next chunk for manual stepping

            # if event.key == pygame.K_RETURN:
            #     for line in coins:
            #         for coin in line:
            #             if coin.color == COLOR2:
            #                 for adj in coin.adjacent:
            #                     if adj not in excited:
            #                         toexcite.append(adj)
            #             coin.release()
            #             coin.draw(screen)
            #     for coin in toexcite:
            #         coin.excite()
            #     excited = toexcite
            #     toexcite = []

        if event.type == GO:
                for line in coins:
                    for coin in line:
                        if coin.color == COLOR2:
                            for adj in coin.adjacent:
                                if adj not in excitednew and adj not in excitedold:
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
