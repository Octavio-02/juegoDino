import pygame
from random import seed
from random import randint

class Cactus():

    def __init__(self,pos_x,image):
        self.pos_x=pos_x
        self.state=0

        self.set_image(image)

    def set_image(self,image):
        if image==0:
            self.cactus=pygame.image.load("assets/images/Cactus1.png")
            self.pos_y=364
            self.hitbox=pygame.Rect(self.pos_x+12, self.pos_y+25, 58, 135)
            self.state=0
        elif image==1:
            self.cactus=pygame.image.load("assets/images/Cactus2.png")
            self.pos_y=364
            self.hitbox=pygame.Rect(self.pos_x+12, self.pos_y+25, 58, 135)
            self.state=0
        elif image==2:
            self.cactus=pygame.image.load("assets/images/Cactus3.png")
            self.pos_y=364
            self.hitbox=pygame.Rect(self.pos_x+12, self.pos_y+25, 58, 135)
            self.state=0
        else:
            self.cactus=pygame.image.load("assets/images/Dactilo1.png")
            if randint(0,2) == 0:
                self.pos_y=340
            else:
                self.pos_y=420
            self.hitbox=pygame.Rect(self.pos_x, self.pos_y+16, 104, 51)
            self.state=1

    def inc_pos_x(self):
        self.pos_x = self.pos_x-8
        self.hitbox=self.hitbox.move(-8,0)

    def get_x(self):
        return self.pos_x

    def set_x(self,pos):
        self.pos_x=pos
    def get_hitbox(self):
        return self.hitbox

    def Draw(self,window,clock):
        if self.state!=0:
            if clock%16<8:
                self.cactus=pygame.image.load("assets/images/Dactilo1.png")
            else:
                self.cactus=pygame.image.load("assets/images/Dactilo2.png")
        window.blit(self.cactus,(self.pos_x,self.pos_y))



        #pygame.draw.rect(window, "red", self.hitbox)
