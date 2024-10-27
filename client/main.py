from world.world import world
from audio import audio
from filehandler import filehandler
import pygame

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
# DISPLAY_W, DISPLAY_H = 1920, 1080
pygame.display.set_caption("Anna's Ants")
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
running = True
clock = pygame.time.Clock()
pygame.mixer.init()
################################# LOAD PLAYER AND SPRITESHEET ###################################

#################################### LOAD THE LEVEL #######################################
world.preload(screen)

################################# GAME LOOP ##########################
while running:
    clock.tick(60)
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    ################################# UPDATE/ Animate SPRITE #################################

    ################################# UPDATE WINDOW AND DISPLAY #################################
    screen.fill((0, 180, 240)) # Fills the entire screen with light blue
    world.render(screen)
    pygame.display.flip()