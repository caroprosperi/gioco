import pygame

BLACK = (0, 0, 0)
class Bottone:
    def __init__(self, color, width, height, pos)-> None:
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        self.pos = pos
        
        pygame.draw.circle(self.image, color, [width/2, height/2], width/2)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]    
        self.rect.y = pos[1]
        
    def draw(self, surf):
        surf.blit(self.image, self.rect)