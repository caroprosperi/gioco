import pygame, sys
from pygame.locals import *
from pallina import Ball
from base import Paddle

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

# ciclo fondamentale
while True:
    
    #ciclo che serve per chiudere il programma quando l'utente vuole chiudere la finestra 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #funzione che serve per rigenerare lo schermo ad ogni giro del ciclo 
    screen.fill("white")
    
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
    
    #if che verifica se la pallina si trova all'interno della finestra oppure no, se è all'interno si può disegnare
    #se invece non è all'interno la pallina non può essere disegnata 
    if posizione_ball_x + r < screen_length and posizione_ball_y + r < screen_height:
        
        pygame.draw.circle(screen, colore_ball, (posizione_ball_x,posizione_ball_y), r)
        posizione_ball_x += velocità_ball
    
    
            
# qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.update()

    # aspetto il prossmo frame
    clock.tick(fps)