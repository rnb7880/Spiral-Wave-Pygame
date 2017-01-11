import pygame
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Coin():
    """
    """
    def __init__(self,x,y,rad):
        self.color = (0, 255, 0)
        self.x =x
        self.y=y
        self.adjacent = []
        self.radius = rad



    def excite(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        self.color = (255,0,0)

    def chain(self):
        self.excite()
        self.release()


    def release(self):
        """
        """
        self.color = (0, 255, 0)

    def draw(self,screen):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    def add(self,coin):
        self.adjacent.append(coin)
    def alert(self):
        for coin in self.adjacent:
            if coin.color != (255,0,0):
                #coin.excite()
                coin.chain()