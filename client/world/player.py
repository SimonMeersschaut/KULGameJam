from .entities import Entity
from filehandler import filehandler

class Player(Entity):
    def __init__(self):
        self.frame_index = 0
    
    def preload_image(self):
        filehandler.preload_tile_set('resources/images/run.set.png', (128, 96))
        self.frames = len(filehandler['resources/images/run.set.png'])
    
    def render(self, screen):
        self.frame_index += 1
        self.frame_index = (self.frame_index) % (self.frames * 5)
        im = filehandler['resources/images/run.set.png'][int(self.frame_index / 5)]
        screen.blit(im, (0,0))

player = Player()