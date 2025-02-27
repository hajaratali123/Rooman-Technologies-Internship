import pygame
import math
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
ANGLE = math.radians(60)  # Convert degrees to radians
SPEED = 2  # Speed of the fish

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Anglerfish Animation")

# Load the anglerfish image safely
IMAGE_PATH = "anglerfish.png"  # Ensure this file is in the same folder
if not os.path.exists(IMAGE_PATH):
    print(f"Error: '{IMAGE_PATH}' not found. Place the image in the script folder.")
    pygame.quit()
    exit()

# Anglerfish Class
class Anglerfish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(IMAGE_PATH)  # Load the anglerfish image
        self.image = pygame.transform.scale(self.image, (100, 60))  # Resize if needed
        self.image = pygame.transform.rotate(self.image, -60)  # Rotate to match movement
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        # Move the fish upward at a 60-degree angle
        self.x += SPEED * math.cos(ANGLE)
        self.y -= SPEED * math.sin(ANGLE)  # Negative because y-coordinates increase downward
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Main loop
def main():
    clock = pygame.time.Clock()
    anglerfish = Anglerfish(WIDTH // 2, HEIGHT - 100)  # Start from bottom center

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        anglerfish.update()

        # Draw
        screen.fill((0, 0, 0))  # Clear the screen with black
        anglerfish.draw(screen)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
