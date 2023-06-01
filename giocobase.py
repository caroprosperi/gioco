import pygame, sys
from pygame.locals import *

pygame.init()
WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('disegni e click')

clock = pygame.time.Clock()
fps = 60

class Miorettangolo:
    def __init__(self, pos, size) -> None:
        self.colore1 = (100,100,100)
        self.colore2 = (255,255,255)
        self.colore = self.colore1
        self.image = pygame.Surface(size)
        # self.rect = self.image.get_rect()
        # self.rect.topleft = pos
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def draw(self):
        self.image.fill(self.colore)
        screen.blit(self.image, self.rect)

    def toggle_color(self):
        if self.colore == self.colore1:
            self.colore = self.colore2
        else:
            self.colore = self.colore1
        self.draw()
    
    def set_color_1(self):
        self.colore = self.colore1
    def set_color_2(self):
        self.colore = self.colore2


class Cerchio:
    def __init__(self, pos, raggio) -> None:
        self.colore1 = (100,100,100)
        self.colore2 = (255,255,255)
        self.colore = self.colore1
        self.image = pygame.Surface((raggio*2, raggio*2))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.center = pos
        self.raggio = raggio

    def draw(self):
        pygame.draw.circle(self.image, self.colore, (self.rect.width/2, self.rect.height/2), self.raggio)
        screen.blit(self.image,self.rect)

    def toggle_color(self):
        if self.colore == self.colore1:
            self.colore = self.colore2
        else:
            self.colore = self.colore1
        self.draw()
    
    def set_color_1(self):
        self.colore = self.colore1
    def set_color_2(self):
        self.colore = self.colore2
    
    def interno(self, pos):
        if ((pos[0]-self.center[0])**2 + (pos[1]-self.center[1])**2)**0.5 <= self.raggio:
            return True
        else:
            return False 


r1 = Miorettangolo((30,30), (60,60))
r1.draw()

r2 = Miorettangolo((100,100), (60,60))
r2.draw()

cerchio = Cerchio((200,200), 20)
cerchio.draw()

pygame.display.flip()

# ciclo fondamentale
while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 tasto sinistro, 2 tasto centrale, 3 tasto destro...
            pos = pygame.mouse.get_pos()
            if r1.rect.collidepoint(pos):
                r1.toggle_color()
            if cerchio.interno(pos):
                cerchio.toggle_color()
            


    # voglio cambiare colore se passo sopra il rettangolo se no lo lascio normale
    pos = pygame.mouse.get_pos()
    if r2.rect.collidepoint(pos):
        r2.set_color_2()
    else:
        r2.set_color_1()
    r2.draw()
    # forse così non è efficientissimo perchè lo disegno ad ogni ciclo, potrei tener traccia dello stato e 
    # verificare se il cursore entra o esce dal rettangolo

    
    # qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.flip()

    # aspetto il prossmo frame
    clock.tick(fps)
