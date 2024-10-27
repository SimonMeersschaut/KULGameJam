from world.world import world
from audio import audio
from filehandler import filehandler
import pygame
from menu import menu

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
# DISPLAY_W, DISPLAY_H = 1920, 1080
pygame.display.set_caption("Anna's Ants")
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
running = True
clock = pygame.time.Clock()
pygame.mixer.init()
mode = 'menu'
################################# LOAD PLAYER AND SPRITESHEET ###################################

#################################### LOAD THE LEVEL #######################################
world.preload(screen)
menu.initialize()

audio.preload('resources/audio/background.mp3')
audio.play('resources/audio/background.mp3')
audio_counter = 0

################################# GAME LOOP ##########################
while running:
    clock.tick(60)
    audio_counter += 1
    if audio_counter > 2040:
        audio_counter = 0
        audio.play('resources/audio/background.mp3')
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mode == 'menu':
                switch = menu.click(pygame.mouse.get_pos())
                if switch:
                    mode = 'game'

    ################################# UPDATE/ Animate SPRITE #################################

    ################################# UPDATE WINDOW AND DISPLAY #################################
    screen.fill((0, 180, 240)) # Fills the entire screen with light blue
    if mode == 'menu':
        menu.render(screen)
    else:
        world.render(screen)
    pygame.display.flip()