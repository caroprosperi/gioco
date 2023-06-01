import pygame
from random import randint
 
BLACK = (0, 0, 0)


class Pallina(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        #set sfondo a trasparente
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        #disegna cerchio
        pygame.draw.circle(self.image, color, [width/2, height/2], width/2)
        
        self.velocity = [randint(6,8),randint(-8,-1)]
        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        if randint(0,1) == 0:
            self.velocity[0] = randint(5,8)
        else:
            self.velocity[0] = randint(-8,-5)

        self.velocity[1] = -self.velocity[1]

    def draw(self, surf):
        surf.blit(self.image, self.rect)
        