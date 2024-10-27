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
        self.y = random.randint(0, 1000)
        self.width = 128
        self.height = 260
        self.delay = delay
        self.animation_frame = 0
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
                # check for dead ants
                for ant in world.ants:
                    if distance((ant.x, ant.y), (self.x + self.width/2, self.y + self.height/2)) < 100:
                        ant.kill()
                # render
                im = filehandler.get_image('resources/images/miereneters.set.png', tile_size=260, index=int(self.animation_frame % 2))
                im = pygame.transform.rotate(im, 90)
                screen.blit(im, (self.x, self.y))

class Foot(Enemy):
    DURATION = 3
    WARNING_TIME =  1
    def __init__(self, delay: int):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 700)
        self.width = 256
        self.height = 256
        self.start_t = time.time() + delay
        self.animation_frame = 0
    
    def render(self, world, screen):
        self.animation_frame += .1
        if time.time() - self.start_t > 0:
            # visible
            if time.time() - self.start_t < Foot.WARNING_TIME:
                # show warning
                im = filehandler.get_image('resources/images/foot.set.png', tile_size=256, index=int(self.animation_frame)%2)
                screen.blit(im, (self.x, self.y))

            else:
                if time.time() - self.start_t > Foot.WARNING_TIME + Foot.DURATION:
                    world.enemies.remove(self)
                else:
                    # PUSH
                    # check for dead ants
                    for ant in world.ants:
                        OFFSET = 10
                        # if collide((ant.x, ant.y, 32, 32), (self.x+OFFSET, self.y+OFFSET, 256-OFFSET, 256-OFFSET)):
                        if distance((ant.x, ant.y), (self.x + self.width/2, self.y + self.height/2)) < 100:
                            ant.kill()
                    # render
                    im = filehandler.get_image('resources/images/foot.set.png', tile_size=256, index=2)
                    screen.blit(im, (self.x, self.y))


class Tuinslang(Enemy):
    DURATION = 3
    WARNING_TIME =  2
    def __init__(self, delay: int):
        self.x = random.randint(0, 1000)
        self.y = 0
        # self.width = 256
        # self.height = 256
        self.start_t = time.time() + delay
        self.animation_frame = 0
    
    def render(self, world, screen):
        self.x += 2
        if time.time() - self.start_t > 0:
            # visible
            if time.time() - self.start_t < Foot.WARNING_TIME:
                # show warning
                im = filehandler.get_image('resources/images/kraan.png')
                screen.blit(im, (self.x-40, self.y))
                screen.blit(im, (self.x-40, self.y))
                im = filehandler.get_image('resources/images/draaiende_kraan.png')
                # pygame.transform.rotate(im, )
                screen.blit(im, (self.x-10, self.y+40))

            else:
                if time.time() - self.start_t > Foot.WARNING_TIME + Foot.DURATION:
                    world.enemies.remove(self)
                else:
                    # show
                    pygame.draw.rect(screen, (45, 175, 255), (self.x, self.y+40, 7, 700))
                    im = filehandler.get_image('resources/images/kraan.png')
                    screen.blit(im, (self.x-40, self.y))
                    screen.blit(im, (self.x-40, self.y))
                    im = filehandler.get_image('resources/images/draaiende_kraan.png')
                    # pygame.transform.rotate(im, )
                    screen.blit(im, (self.x-10, self.y+40))

                    for ant in world.ants:
                        if self.x+ 7 > ant.x > self.x:
                            ant.kill()