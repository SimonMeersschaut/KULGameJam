import time
import pygame
from filehandler import filehandler


class Animation:
    DURATION = 2
    def __init__(self, on_done=None, time_offset: float = 0):
        self.start_t = time.time() + time_offset
        self.on_done = on_done
    
    def finish(self, camera, world):
        camera.delta_t = 1/60 # default speed
        camera.allow_rendering = True # enable other rendering
        if self.on_done is not None:
            self.on_done()
        world.animations.remove(self)
        # print(world.animations)

    def render(self, camera, screen, world):
        # camera.delta_t = (1/60)/10
        if time.time() - self.start_t > type(self).DURATION:
            self.finish(camera, world)

class SlideAnimation(Animation):
    # DURATION = 10
    def __init__(self, order:int, index: int, on_done=None):
        self.order = order
        self.index = index
        super().__init__(on_done, time_offset = 0)
    
    def render(self, camera, screen, world):
        if self.order == 0:
            # first slide
            # render image   
            camera.delta_t = 0
            im = filehandler.get_image(f'resources/images/slides/slide_{self.index}.png')
            screen.blit(im, (0, 0))
            camera.allow_rendering = False
            # h s= 10
            # w = (time.time() - self.start_t)/SlideAnimation.DURATION*1280
            # pygame.draw.rect(screen, (color), (0, 720-h, w, h))
            # super().render(camera, screen, world)

            if time.time() - self.start_t > 3:
                if pygame.mouse.get_pressed()[0]:
                    for animation in world.animations:
                        if type(animation) == SlideAnimation:
                            animation.start_t = time.time()
                            animation.order -= 1
                    # close animation
                    self.finish(camera, world)

class RageAnimation(Animation):
    DURATION = 1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = pygame.font.Font('resources/pixel.ttf', 70)
        self.text_rendered = font.render('Granny is back!!', True, (0,0,0))
    
    def render(self, camera, screen, world):
        camera.delta_t = (1/60)/10
        # if time.time() - self.start_t > type(self).DURATION:
        #     self.finish(camera, world)
        
        super().render(camera, screen, world)
        # pygame.draw.rect(screen, (0,0,0), (50, 50, 50, 50))
        screen.blit(self.text_rendered, (350, 10))

class DeadAnimation(Animation):
    def __init__(self, x, y, on_done=None):
        self.x = x
        self.y = y
        # input('initialized')
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
        self.text_rendered = font.render('Game Over!', True, (0,0,0))
    
    # def finish(self, camera, world):
        # camera.delta_t = 1/60 # default speed
        # world.animation = False
        # if self.on_done is not None:
        #     self.on_done()
        # world.finish()
        # ...
    
    def render(self, camera, screen, world):
        # camera.delta_t = 0
        camera.delta_t = (1/60)/10
        if time.time() - self.start_t > type(self).DURATION:
            self.finish(camera, world)
        
        # pygame.draw.rect(screen, (0,0,0), (50, 50, 50, 50))
        screen.blit(self.text_rendered, (450, 10))