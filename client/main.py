from world.world import world
from audio import audio
import pygame

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 480, 270
screen = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
pygame.mixer.init()
################################# LOAD PLAYER AND SPRITESHEET ###################################

#################################### LOAD THE LEVEL #######################################
world.preload()

################################# GAME LOOP ##########################
while running:
    clock.tick(60)
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            world.spray(pygame.mouse.get_pos())

    ################################# UPDATE/ Animate SPRITE #################################

    ################################# UPDATE WINDOW AND DISPLAY #################################
    screen.fill((0, 180, 240)) # Fills the entire screen with light blue
    world.render(screen)
    pygame.display.flip()