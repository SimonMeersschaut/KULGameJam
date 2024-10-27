import time
import pygame
from filehandler import filehandler


class Animation:
    DURATION = 2
    def __init__(self, on_done=None):
        self.start_t = time.time()
        self.on_done = on_done
    
    def finish(self, camera, world):
        camera.delta_t = 1/60 # default speed
        world.animations.remove(self)
        if self.on_done is not None:
            self.on_done()
    
    def render(self, camera, screen, world):
        camera.delta_t = (1/60)/10
        if time.time() - self.start_t > type(self).DURATION:
            self.finish(camera, world)
        pygame.draw.rect(screen, (0,0,0), (50, 50, 50, 50))

class RageAnimation(Animation):
    DURATION = 1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = pygame.font.Font('resources/pixel.ttf', 70)
        self.text_rendered = font.render('FIGHT!', True, (100,0,0))
    
    def render(self, camera, screen, world):
        # camera.delta_t = (1/60)/10
        if time.time() - self.start_t > type(self).DURATION:
            self.finish(camera, world)
        
        # pygame.draw.rect(screen, (0,0,0), (50, 50, 50, 50))
        screen.blit(self.text_rendered, (400, 200))

class DeadAnimation(Animation):
    def __init__(self, x, y, on_done=None):
        self.x = x
        self.y = y
        super().__init__(on_done)

    def render(self, camera, screen, world):
            # camera.delta_t = 0
            if time.time() - self.start_t > type(self).DURATION:
                self.finish(camera, world)
            
            # pygame.draw.rect(screen, (0,0,0), (50, 50, 50, 50))
            im = filehandler.get_image('resources/images/ant.set.png', tile_size=128, index=3)
            screen.blit(im, (self.x-(128/2), self.y-(128/2)))

class GameOverAnimation(Animation):
    def __init__(self, on_done=None):
        super().__init__(on_done)
        font = pygame.font.Font('resources/pixel.ttf', 70)
        self.text_rendered = font.render('Game Over!', True, (100,0,0))
    
    def finish(self, camera, world):
        # camera.delta_t = 1/60 # default speed
        # world.animation = False
        # if self.on_done is not None:
        #     self.on_done()
        world.finish()
    
    def render(self, camera, screen, world):
        # camera.delta_t = 0
        camera.delta_t = (1/60)/10
        if time.time() - self.start_t > type(self).DURATION:
            self.finish(camera, world)
        
        # pygame.draw.rect(screen, (0,0,0), (50, 50, 50, 50))
        screen.blit(self.text_rendered, (400, 200))