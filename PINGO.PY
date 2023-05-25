import pygame, sys
from pygame.locals import *
from pallina import Ball
from base import Paddle
from random import randint 

#parametri finestra 
screen_height = 400
screen_length = 600

# settaggi base finestra
WINDOW_SIZE = (screen_length, screen_height)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Finestra Base')
screen.fill("white")

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60

#parametri della pallina
posizione_ball_x = 300
posizione_ball_y = 300
velocità_ball = 10
r =  10
colore_ball= (0,0,0)

#parametri dei blocchi 
lunghezza = 50
altezza = 25
marginefinale = 60
margineblocchi = 2
colori = [(224,175,238	), (94,134,193),(227,11,92),(222, 4, 4), (99,151,208) ]
pos_iniziali= [-10, -30, -43, -25, -14]

ball = Ball(colore_ball, 2*r, 2*r)
ball.rect.x = posizione_ball_x
ball.rect.y = posizione_ball_y

paddleA = Paddle(colore_ball, 10, 100) #---> cambio colore paddle 
paddleA.rect.x = 300
paddleA.rect.y = 320



all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)
# ciclo fondamentale
while True:
    
    #ciclo che serve per chiudere il programma quando l'utente vuole chiudere la finestra 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
   
    
    #parametri blocchi variabili 
    pos_x =50
    pos_y = 0
    
    #comandi per creare e poiszionare i blocchi sullo schermo 
    for colore, pos_iniziale in zip(colori, pos_iniziali):
        pos_y += altezza + margineblocchi
        last_block_x = pos_iniziale
        while last_block_x + lunghezza< screen_length- marginefinale:
            pygame.draw.rect(screen, colore, (last_block_x + lunghezza+ margineblocchi, pos_y, lunghezza, altezza))
            last_block_x = last_block_x + lunghezza + margineblocchi
    
    all_sprites_list.update()
    
    if ball.rect.right >= screen_length:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    # if ball.rect.y > 490:
    if ball.rect.bottom > screen_length:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]    
    
     #funzione che serve per rigenerare lo schermo ad ogni giro del ciclo 
    screen.fill("white")
    
    ball.draw(screen)
    
    pygame.display.flip()

            
# qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.update()

    # aspetto il prossmo frame
    clock.tick(fps)