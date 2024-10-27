from filehandler import filehandler
import pygame
from .bounding_boxes import collide, distance
import random
import time

class Enemy:
    def __init__(self):
        ...

class AntEater(Enemy):
    DELAY = 10 # seconds between waves
    WARNING_TIME = 2
    # PREVIEW = 3
    def __init__(self, delay: int):
        # self.delay = delay
        self.x = 0
        self.y = random.randint(0, 500)
        self.width = 128
        self.height = 260 #TODO
        self.delay = delay
        self.animation_frame = 0

    def initialize(self):
        self.start_t = time.time() + self.delay
    
    def render(self, world, screen):
        self.animation_frame += .1
        if time.time() - self.start_t > 0:
            # visible
            if time.time() - self.start_t < AntEater.WARNING_TIME:
                # show warning
                if int(self.animation_frame % 2) == 0:
                    im = filehandler.get_image('resources/images/uitroepteken1.png')
                else:
                    im = filehandler.get_image('resources/images/uitroepteken2.png')
                screen.blit(im, (self.x, self.y))
            else:
                # RUN!
                self.x += 5
                if self.x > 1920:
                    # out of screen
                    # remove enemy
                    world.enemies.remove(self)
                # check for dead enemies
                for ant in world.ants:
                    if distance((ant.x, ant.y), (self.x + self.width/2, self.y + self.height/2)) < 100:
                        ant.kill()
                # render
                im = filehandler.get_image('resources/images/miereneters.set.png', tile_size=260, index=int(self.animation_frame % 2))
                im = pygame.transform.rotate(im, 90)
                screen.blit(im, (self.x, self.y))
