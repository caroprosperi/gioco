import pygame
BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the Paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        #self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # Check that you are not going too far (off the screen)
        if self.rect.right < 100:
            self.rect.right = 100

    def moveRight(self, pixels):
        self.rect.x += pixels
        # Check that you are not going too far (off the screen)
        if self.rect.right > 600:
            self.rect.right = 600

    def draw(self, surf):
        surf.blit(self.image, self.rect)
