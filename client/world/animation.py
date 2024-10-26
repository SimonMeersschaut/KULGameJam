import time
import pygame

class Animation:
    DURATION = 5
    def __init__(self, on_done):
        self.start_t = time.time()
        self.on_done = on_done
    
    def finish(self, camera, world):
        self.on_done()
        camera.delta_t = 1/60 # default speed
        world.animation = False
        del self
    
    def render(self, camera, screen, world):
        camera.delta_t = (1/60)/10
        print('running animation')
        print('FIGHT')
        if time.time() - self.start_t > type(self).DURATION:
            self.finish(camera, world)
        pygame.draw.rect(screen, (0,0,0), (50, 50, 50, 50))