import pygame
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Coin():
    """
    """
    def __init__(self,x,y,rad,color1,color2):
        self.color = (0, 255, 0)
        self.x =x
        self.y=y
        self.adjacent = []
        self.radius = rad
        self.c1=color1
        self.c2=color2



    def excite(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        self.color = self.c2

    def chain(self):
        self.excite()
        self.release()


    def release(self):
        """
        """
        self.color = self.c1

    def draw(self,screen):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    def add(self,coin):
        self.adjacent.append(coin)
    def alert(self):
        for coin in self.adjacent:
            if coin.color != self.c1:
                #coin.excite()
                coin.chain()