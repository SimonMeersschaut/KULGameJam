import pygame
from world import world

# Initialize Pygame
pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Create the display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tile Map Renderer")

# load map
world = world.World()
# map_surface = world.load_map()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Blit the map surface onto the screen
    screen.blit(world.image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
