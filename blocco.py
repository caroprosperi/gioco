import pygame
from random import randint
 
BLACK = (0, 0, 0)


class Block(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0,0, width, height])
        
        self.velocity = [0,0]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def draw(self, surf):
        surf.blit(self.image, self.rect)