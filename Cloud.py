import pygame

class Cloud():

    def __init__(self,adx,ady):
        self.pos_x=1600+adx
        self.pos_y=100+ady

        self.cloud1=pygame.image.load("assets/images/Nube1.png")

    def inc_pos_x(self):
        self.pos_x= self.pos_x-8

    def random_pos_y(self,add):
        self.pos_y = 100+add

    def get_x(self):
        return self.pos_x

    def set_x(self,pos):
        self.pos_x=pos

    def Draw(self,window):
        window.blit(self.cloud1,(self.pos_x,self.pos_y))
