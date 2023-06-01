import pygame
from random import randint
 
BLACK = (0, 0, 0)

#abbiamo messo la classe blocco nel main perchè importandola da un'altro file ci dava dei problemi
#questa è la classe Blocco su un file separato dal main  
class Blocco(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
            
        #set sfondo a trasparente
        self.image = pygame.Surface([width, height])

        #disegna rettangolo
        pygame.draw.rect(self.image, color, [0,0, width, height])
        
        self.velocity = [0,0]
        
        self.rect = self.image.get_rect()

    def draw(self, surf):
        surf.blit(self.image, self.rect)