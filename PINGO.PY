import pygame, sys
from pygame.locals import *
from pallina import Ball
from base import Paddle
from random import randint 
from blocco import Block

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
posizione_ball_x = 290
posizione_ball_y = 300
velocità_ball = 10
r =  10
colore_ball= (255,0,0)

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

paddleA = Paddle(colore_ball, 100, 10 ) #---> cambio colore paddle 
paddleA.rect.x = 300
paddleA.rect.y = 330

  

#parametri blocchi variabili 
pos_x =50
pos_y = 0
listaBlocchi= []

#comandi per creare e poiszionare i blocchi sullo schermo 
for colore, pos_iniziale in zip(colori, pos_iniziali):
    pos_y += altezza + margineblocchi
    last_block_x = pos_iniziale
    while last_block_x + lunghezza< screen_length- marginefinale:
        b = Block(colore, lunghezza, altezza)
        listaBlocchi.append(b)
        b.rect.x = last_block_x + lunghezza+ margineblocchi
        b.rect.y = pos_y + altezza + margineblocchi
        last_block_x = last_block_x + lunghezza + margineblocchi

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)
all_sprites_list.add(paddleA)
for blocco in listaBlocchi:
    all_sprites_list.add(blocco)
    
# ciclo fondamentale
while True:
    
    #ciclo che serve per chiudere il programma quando l'utente vuole chiudere la finestra 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddleA.moveRight(5)
    if keys[pygame.K_LEFT]:
        paddleA.moveLeft(5)
    
    
    all_sprites_list.update()
    
    if ball.rect.right >= screen_length:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    # if ball.rect.y > 490:
    if ball.rect.bottom > screen_height+3*r:
        ball.velocity[1] = 0
        ball.velocity[0] = 0
        paddleA.rect.x = 250 #--> modifico metto parametri
        paddleA.rect.y = 330
        ball.rect.x = posizione_ball_x
        ball.rect.y = posizione_ball_y
        
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]    
        
    if pygame.sprite.collide_mask(ball, paddleA):
        ball.bounce()
    for blocco in listaBlocchi:
        if pygame.sprite.collide_mask(ball,blocco):
            
        
    
     #funzione che serve per rigenerare lo schermo ad ogni giro del ciclo 
    screen.fill("navy")
    
    ball.draw(screen)
    paddleA.draw(screen)
    for blocco in listaBlocchi:
        blocco.draw(screen)
    
  
    
    

    pygame.display.flip()
    # aspetto il prossmo frame
    clock.tick(fps)