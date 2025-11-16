import pygame
import sys
import assets

# Initialize Pygame
pygame.init()

# Create a window (width, height)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Pygame Window")
clock = pygame.time.Clock()

image = pygame.image.load("assets/green.png")

# Starting position
x = 0
y = 100

# Speed (pixels per frame)
speed_x = 3
speed_y = 0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (optional)
    screen.fill((30, 30, 30))

    # Update position
    x += speed_x
    y += speed_y

    # Draw the image at position (100, 100)
    screen.blit(image, (x, y))

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second
    