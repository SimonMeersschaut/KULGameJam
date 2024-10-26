import pygame
import random
from filehandler import filehandler
from audio import audio
from math import cos, sin, degrees
import numpy as np
from math import atan2, pi, sqrt
from .food import *

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

def slerp(v0, v1, t):
    """
    Spherical linear interpolation between two normalized vectors v0 and v1.
    t is the interpolation parameter, typically between 0 (returns v0) and 1 (returns v1).
    """
    # Ensure vectors are normalized
    v0 = v0 / np.linalg.norm(v0)
    v1 = v1 / np.linalg.norm(v1)

    # Compute the angle theta between v0 and v1
    dot_product = np.dot(v0, v1)
    dot_product = np.clip(dot_product, -1.0, 1.0)  # Clamp to avoid numerical issues

    theta = np.arccos(dot_product)  # Angle between vectors in radians

    # If theta is very small, use linear interpolation to avoid division by zero in sin(theta)
    if theta < 1e-10:
        return (1 - t) * v0 + t * v1

    # SLERP formula
    sin_theta = np.sin(theta)
    v0_factor = np.sin((1 - t) * theta) / sin_theta
    v1_factor = np.sin(t * theta) / sin_theta

    return v0_factor * v0 + v1_factor * v1

class World:
    TILE_SIZE = 48
    def __init__(self):
        self.i = 0
        self.food = [Apple(10, 10), Pizza(50, 50), Druif(100, 100)]

    def preload(self):
        # load images
        self.ants = [Ant(random.randint(0, 10), random.randint(0, 10)) for _ in range(1)]
        self.heat_map = np.zeros((11, 11))
    
    def spray(self, pos: tuple[int, int]):
        if pos[0] > 0 and pos[1] > 0:
            tile_x = round(pos[0] / World.TILE_SIZE)
            tile_y = round(pos[1] / World.TILE_SIZE)
            self.heat_map[tile_y][tile_x] = 1

    def update(self):
        camera.distance += .01
        for ant in self.ants:
            ant.update_direction()
        self.heat_map -= .01
        self.heat_map = np.maximum(self.heat_map, 0)
        for ant in self.ants:
            ant.update()
        self.i += 1

    def render(self, screen: object) -> None:
        """Render the entire world."""
        self.update()
        for ant in self.ants:
            ant.render(screen)
        
        meter.render(screen)
        
        # render spray
        for y, row in enumerate(world.heat_map):
            for x, tile in enumerate(world.heat_map[y]):
                x_pos, y_pos = (x*World.TILE_SIZE, y*World.TILE_SIZE)
                if tile > 0:
                    pygame.draw.rect(screen, (0,0,0), (x_pos, y_pos, 64, 64))
        
        for food in self.food:
            food.render(screen)

class Camera:
    def __init__(self):
        self.distance = 1
    
class Meter:
    METER_IMAGE = 'resources/images/meter.png'
    HANDS_IMAGE = 'resources/images/hands.png'
    BACKGROUND_COLOR = (181, 240, 224)
    def __init__(self):
        self.x = 2
        self.y = 416
        self.score = 0
        self.animation_frame = 0
    
    def calc_meter(self, score):
        if score <= 100:
            return score
        elif score <= 200:
            return 100 + (score-100)*1.27
        elif score <= 300:
            return 227 + (score-200)*1.45
        elif score <= 400:
            return 345 + (score-300)*.95
        else:
            return 440 #max

    def render(self, screen):
        # draw meter
        self.score += 1
        # score
        pygame.draw.rect(screen, (100, 0, 0), (17+self.x, 10+self.y, self.calc_meter(self.score), 50))
        # water droplets
        pygame.draw.rect(screen, Meter.BACKGROUND_COLOR, (450+self.x, self.y + 5, 20, 15))
        im = filehandler.get_image(Meter.METER_IMAGE)
        screen.blit(im, (self.x, self.y))
        # draw granny
        im = filehandler.get_image(Meter.HANDS_IMAGE)
        screen.blit(im, (self.x, self.y-9))
        

class Ant:
    IMAGE = 'resources/images/ant.set.png'
    SIZE = .5
    SPEED = 5
    ROTATION_SPEED = .05
    MAX_DISTANCE = 100**2
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.theta = 0
        self.dir = np.array([1, 0])
        self.frame_index = 0

    def choose_target(self) -> tuple:
        max_score = -float('inf')
        max_tile = None
        for tile_y, row in enumerate(world.heat_map):
            for tile_x, tile in enumerate(row):
                xpos, ypos = (tile_x*World.TILE_SIZE, tile_y*world.TILE_SIZE)
                dist = sqrt((xpos-self.x)**2 + (ypos-self.y)**2)
                score = tile/dist
                if score >= max_score:
                    max_tile = (xpos, ypos)
                    max_score = score

        if max_tile is None:
            raise RuntimeError('No found!!')
        return max_tile
    
    def update_direction(self):
        target = self.choose_target()
        dir = np.array([target[0]-self.x, target[1]-self.y])
        norm = np.linalg.norm(dir)

        normalized_vector = dir/norm
        self.dir = slerp(self.dir, normalized_vector, Ant.ROTATION_SPEED)
        self.theta = atan2(self.dir[1], self.dir[0])
    
    def update(self):
        # move forward
        self.update_direction()
        self.x += self.dir[0]*Ant.SPEED
        self.y += self.dir[1]*Ant.SPEED
    
    def render(self, screen):
        self.frame_index += .1
        im = filehandler.get_image(Ant.IMAGE, size=Ant.SIZE*(1/camera.distance), index=int(self.frame_index % 3))
        _, _, w, h = im.get_rect()
        # im = pygame.transform.scale(im, (w*Ant.SIZE*(1/camera.distance), h*Ant.SIZE*(1/camera.distance)))
        im, new_rect = rot_center(im, 90-degrees(self.theta), self.x, self.y)
        screen.blit(im, new_rect)
        # pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x + cos(self.target_theta)*100, self.y + sin(self.target_theta)*100))
    
    def __del__(self):
        world.ants.remove(self)

world = World()
camera = Camera()
meter = Meter()