import pygame
from random import randint
 
BLACK = (0, 0, 0)

# class Palla():
#     def __init__(self, screen, color, pos, size) -> None:
#         self.screen = screen
#         self.color = color
#         self.surf = pygame.Surface(size)
#         self.rect = pygame.Rect(pos, size)
#         self.raggio = self.rect.size[0] / 2
#         self.v_orizz = 5
#         self.v_vert = 3

#     def draw(self):
#         pygame.draw.circle(self.surf, self.colore, (self.raggio, self.raggio), self.raggio)
#         self.screen.blit(self.surf,self.rect)

#     def muovi(self):
#         self.rect.x += self.v_orizz[0]
#         self.rect.y += self.v_vert[1]




class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.circle(self.image, color, [width/2, height/2], width/2)
        
        self.velocity = [randint(6,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        if randint(0,1) == 0:
            self.velocity[0] = randint(5,8)
        else:
            self.velocity[0] = randint(-5,-8)

        self.velocity[1] = -self.velocity[1]

    def draw(self, surf):
        surf.blit(self.image, self.rect)