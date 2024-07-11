import pygame
from Player import Player
from Floor import Floor
from Curtain import Curtain
from Cloud import Cloud
from Cactus import Cactus

from random import seed
from random import randint

SKY = (15,210,245)

if __name__ == "__main__":
    pygame.init()
    seed(1)

    #Disposición de la ventana
    window=pygame.display.set_mode(size=(1600,600))
    pygame.display.set_caption("Dino Game")
    window.fill(SKY)

    #Reloj de Juego
    clock=0
    game_over=0
    speed=0

    #Creación del jugador
    player=Player()
    player.draw(window,clock)
    curtain=Curtain()

    #Creación del Piso
    floor=Floor(0)
    floor_extra=Floor(2400)
    floor.draw(window)

    #Variable de control de eventos
    block = 0
    event_clock = 0

    #Nubes
    clouds=[Cloud(0,0),Cloud(16*randint(32,48),randint(-50,50)),Cloud(32*randint(32,48),randint(-50,50))]

    #Cactus
    cactus=[Cactus(1600+randint(0,600),randint(0,2)),Cactus(2400+randint(0,600),randint(0,2)),Cactus(3200+randint(0,600),randint(0,2))]

    while game_over==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if block == 0:
                    if event.key == pygame.K_SPACE:
                        block = 1
            if event.type == pygame.KEYDOWN and block==0:
                if event.key == pygame.K_DOWN:
                    player.crouch()
            if event.type == pygame.KEYUP and block==0:
                if event.key == pygame.K_DOWN:
                    player.straight()

        #Salto del juagdor
        if block == 1:
            if event_clock<22:
                player.inc_pos_y()
            elif event_clock>=22 and event_clock<32:
                player.dec_pos_y(0)
            elif event_clock>=32 and event_clock < 37:
                player.dec_pos_y(2)
            elif event_clock>=37 and event_clock < 40:
                player.dec_pos_y(10)
            if event_clock == 40:
                block = 0
                event_clock = 0
            else:
                event_clock = event_clock + 1

        #Movimiento del suelo
        floor.inc_pos_x()
        floor_extra.inc_pos_x()
        if floor.get_x() == -800:
            floor_extra.set_x(1600)
        if floor_extra.get_x() == -800:
            floor.set_x(1600)

        #Movimiento de las nubes
        for i in clouds:
            i.inc_pos_x()
            if i.get_x()<-264:
                i.set_x(1600+8*randint(1,12))
                i.random_pos_y(randint(-50,50))

        #Movimiento de los cactus
        for i in range(0,3,1):
            cactus[i].inc_pos_x()
            if cactus[i].get_x()<-83:
                if i==0:
                    cactus[i].set_x(2400+randint(0,800))
                    cactus[i].set_image(randint(0,4))
                else:
                    cactus[i].set_x(cactus[i-1].get_x()+randint(350,800))
                    cactus[i].set_image(randint(0,4))

        #clock
        clock=clock+1
        if clock==500:
            clock=0
            if speed<18:
                speed=speed+1

        #Checkeo de Colision
        for i in cactus:
            if game_over==0:
                game_over=player.get_hitbox().colliderect(i.get_hitbox())

        #Dibujo de los objetos
        window.fill(SKY)

        floor.draw(window)
        floor_extra.draw(window)
        if block==0:
            pass
            #curtain.draw(window,SKY)
        player.draw(window,clock)
        for i in clouds:
            i.Draw(window)
        for i in cactus:
            i.Draw(window,clock)
        pygame.display.flip()
        pygame.time.wait(20-speed)
