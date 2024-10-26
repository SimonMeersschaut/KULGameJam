# import pygame
# from . import loader
from filehandler import filehandler
from audio import audio
from math import cos, sin
import numpy as np

class World:
    TILE_SIZE = 64
    def __init__(self):
        ...
        # filehandler.preload_tile_set('resources/images/tiles.set.png', World.TILE_SIZE)
        # audio.preload('resources/audio/background.ogg')

    def preload(self):
        # load images
        filehandler.load_image('resources/images/ant.png')
        self.ants = [Ant()]
        self.heat_map = np.zeros((10, 10))
    
    def spray(self, pos: tuple[int, int]):
        tile_x = round(pos[0] / 480 * 10)
        tile_y = round(pos[1] / 270 * 10)
        self.heat_map[tile_x][tile_y] = 1

    def update(self):
        for ant in self.ants:
            ant.update()
    
    def render(self, screen: object) -> None:
        """Render the entire world."""
        self.update()
        for ant in self.ants:
            ant.render(screen)

class Ant:
    IMAGE = 'resources/images/ant.png'
    SIZE = .5
    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.target_theta = 1.5
    
    def update(self):
        # claculate target theta
        

        # rotate towards target theta
        diff = self.target_theta - self.theta
        if diff > .1:
            self.theta += .01
        elif diff < -.1:
            self.theta -= .01

        # move forward
        self.x += cos(self.theta)
        self.y += sin(self.theta)
    
    def render(self, screen):
        im = filehandler.get_image(Ant.IMAGE, size=Ant.SIZE)
        screen.blit(im, (self.x, self.y))
    
    def __del__(self):
        world.ants.remove(self)

world = World()