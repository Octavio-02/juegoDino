import pygame

class Floor():

    def __init__(self,x):
        self.pos_y = 455
        self.pos_x = x

        self.image=pygame.image.load("assets/images/Floor.png")

    def set_x(self,pos):
        self.pos_x=pos

    def get_x(self):
        return self.pos_x

    def inc_pos_x(self):
        self.pos_x = self.pos_x-8

    def draw(self,window):
        window.blit(self.image,(self.pos_x,self.pos_y))
