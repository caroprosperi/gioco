import pygame

BLACK = (0, 0, 0)

class Base(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        
        super().__init__()
        
        #set lo sfondo a trasparente
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        #self.image.set_colorkey(BLACK)

        #disegna la base
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
       #controlla se si esce dallo schermo
        if self.rect.right < 100:
            self.rect.right = 100

    def moveRight(self, pixels):
        self.rect.x += pixels
        #controlla se esce dallo schermo
        if self.rect.right > 600:
            self.rect.right = 600

    def draw(self, surf):
        surf.blit(self.image, self.rect)
