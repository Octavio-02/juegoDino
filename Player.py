import pygame

STRAIGHT = 0
CROUCH = 1

class Player():
    def __init__(self):
        self.state=STRAIGHT
        self.pos_x = 100
        self.pos_y = 344

        self.hitbox=pygame.Rect(self.pos_x+50,self.pos_y,80,150)

        self.dino2=pygame.image.load("assets/images/Dino2.png")
        self.dino3=pygame.image.load("assets/images/Dino3.png")
        self.dinocrouch=pygame.image.load("assets/images/DinoCrouch.png")
        self.dinocrouch2=pygame.image.load("assets/images/DinoCrouch2.png")

    def inc_pos_y(self):
        self.pos_y = self.pos_y-10
        self.hitbox=self.hitbox.move(0,-10)

    def dec_pos_y(self,added):
        self.pos_y = self.pos_y+10+added
        self.hitbox=self.hitbox.move(0,10+added)

    def get_pos_y(self):
        return self.pos_y

    def get_pos_x(self):
        return self.pos_x

    def get_hitbox(self):
        return self.hitbox

    def crouch(self):
        self.state = CROUCH
        self.hitbox=pygame.Rect(self.pos_x,self.pos_y+70,239,105)

    def straight(self):
        self.state = STRAIGHT
        self.hitbox=pygame.Rect(self.pos_x+50,self.pos_y,80,150)

    def draw(self,window,clock):
        if self.state == STRAIGHT:
            if clock%16<8:
                window.blit(self.dino2,(self.pos_x,self.pos_y))
            else:
                window.blit(self.dino3,(self.pos_x,self.pos_y))
        else:
            if clock%16<8:
                window.blit(self.dinocrouch,(self.pos_x,self.pos_y))
            else:
                window.blit(self.dinocrouch2,(self.pos_x,self.pos_y))

        #pygame.draw.rect(window, "blue", self.hitbox)
