from world import world
import pygame
# from spritesheet import Spritesheet


################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 480, 270
screen = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()

################################# LOAD PLAYER AND SPRITESHEET###################################

#################################### LOAD THE LEVEL #######################################
world = world.World()

################################# GAME LOOP ##########################
while running:
    clock.tick(60)
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass
        #     if event.key == pygame.K_LEFT:
        #         player.LEFT_KEY, player.FACING_LEFT = True, True
        #     elif event.key == pygame.K_RIGHT:
        #         player.RIGHT_KEY, player.FACING_LEFT = True, False
        #
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         player.LEFT_KEY = False
        #     elif event.key == pygame.K_RIGHT:
        #         player.RIGHT_KEY = False

    ################################# UPDATE/ Animate SPRITE #################################

    ################################# UPDATE WINDOW AND DISPLAY #################################
    screen.fill((0, 180, 240)) # Fills the entire screen with light blue
    screen.blit(world.image, (0, 0))
    pygame.display.flip()