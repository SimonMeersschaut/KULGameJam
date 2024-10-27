import pygame
import random
from filehandler import filehandler
from audio import audio
from math import degrees
import numpy as np
from math import atan2
from .food import *
import time
from .animation import RageAnimation, DeadAnimation, GameOverAnimation
from .enemies import *
from .rounds import LEVELS

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
        # self.i = 0
        self.wave = 0
        self.level = 0
        self.animations = []
        self.score = 0
        self.rage = False
        self.running = True
        self.food = []
        self.enemies = []
        self.wave_data = {}
        self.last_wave_index = 0
    
    def load_wave(self, screen):
        self.wave_data = LEVELS[self.level][meter.wave_index]
        self.food = self.wave_data['food']
        if meter.wave_index == 0 and self.level == 0:
            # reset ants
            self.ants = [Ant()]
    
    def run_animation(self, animation):
        self.animations.append(animation)
    
    def do_rage(self, index:int):
        self.last_wave_index = index
        world.run_animation(RageAnimation(
            on_done=lambda: world.execute_rage(self.last_wave_index)
        ))
    
    def execute_rage(self, index:int):
        self.rage = True
        print(self.wave_data['enemies'])
        self.enemies += self.wave_data['enemies']
    
    def preload(self, screen):
        # load images
        meter.initialize(screen)
        self.load_wave(screen)

    def update(self, screen):
        if world.rage and self.enemies == []:
            self.rage = False
            self.load_wave(screen)
        
        for ant in self.ants:
            ant.update_direction()
        for ant in self.ants:
            ant.update()

    def render(self, screen: object) -> None:
        """Render the entire world."""
        # animation
        if len(self.animations) > 0:
            for animation in self.animations:
                animation.render(camera, screen, self)
        # update entities
        self.update(screen)
        # render
        for enemy in self.enemies:
            enemy.render(self, screen)
        for ant in self.ants:
            ant.render(screen)

        meter.render(screen)
        
        for food in self.food:
            food.render(screen)
        ...
    
    def finish(self):
        self.running = False
        exit()

class Camera:
    def __init__(self):
        # self.scale = .5
        self.delta_t = 1/60
    
class Meter:
    METER_IMAGE = 'resources/images/meter.png'
    HANDS_IMAGE = 'resources/images/hands.png'
    GRANNY_IMAGE = 'resources/images/granny.png'
    METER_SPEED = 10 # points/second
    BACKGROUND_COLOR = (181, 240, 224)
    def __init__(self):
        self.x = 700
        self.y = 600
        self.animation_frame = 0
        self.score = 0 #TODO
        self.wave_index = 0
    
    def initialize(self, screen):
        w, h = screen.get_size()
        self.x = w/2 - (512/2)
        self.y = h - 64
    
    def calc_meter(self, score):
        if score <= 100:
            return score
        elif score <= 200:
            return 100 + (score-100)*1.27
        elif score <= 300:
            return 228 + (score-200)*1.2
        elif score <= 400:
            return 345 + (score-300)*.95
        else:
            return 440 #max

    def render(self, screen):
        # draw meter
        # udpate score
        w = self.calc_meter(self.score)
        if not world.rage:
            self.score += camera.delta_t*Meter.METER_SPEED
        # check for rage
        if self.score - 100*(self.wave_index+1) >= 0:
            world.do_rage(self.wave_index)
            self.wave_index += 1
            
        # draw granny head
        im = filehandler.get_image(Meter.GRANNY_IMAGE)
        screen.blit(im, (self.x, self.y-170))
        # meter
        color = (200, 0, 0)
        if world.rage:
            color = tuple([random.randint(0, 255) for _ in range(3)])

        pygame.draw.rect(screen, (100, 100, 150), (17+self.x, 10+self.y, 440, 50))
        pygame.draw.rect(screen, color, (17+self.x, 10+self.y, self.calc_meter(w), 50))
        # water droplets
        pygame.draw.rect(screen, Meter.BACKGROUND_COLOR, (450+self.x, self.y + 5, 20, 15))
        im = filehandler.get_image(Meter.METER_IMAGE)
        screen.blit(im, (self.x, self.y))
        # draw granny
        im = filehandler.get_image(Meter.HANDS_IMAGE)
        screen.blit(im, (self.x, self.y-9))

class Ant:
    IMAGE = 'resources/images/ant.set.png'
    SIZE = .25
    SPEED = 300
    ROTATION_SPEED = 3
    WANDERING_DIST = 10000
    MAX_DISTANCE = 100**2
    EATING_DISTANCE = 3000
    EATING_TIMEOUT = 1
    def __init__(self, ant_index=0):
        self.x = 1920/2
        self.y = 1080/2
        self.width = 128
        self.height = 128
        self.theta = 0
        self.dir = np.array([1, 0])
        self.frame_index = 0
        self.wandering_dist = Ant.WANDERING_DIST
        self.eating_timeout = 0
        self.speed = Ant.SPEED # * max(.1, random.random())

    def update_direction(self):
        target = pygame.mouse.get_pos()
        dist = (self.x-target[0])**2 + (self.y-target[1])**2
        if dist < self.wandering_dist:
            # wandering
            ...
        else:
            dir = np.array([target[0]-self.x, target[1]-self.y])
            norm = np.linalg.norm(dir)

            normalized_vector = dir/norm
            self.dir = slerp(self.dir, normalized_vector, Ant.ROTATION_SPEED*camera.delta_t)
            self.theta = atan2(self.dir[1], self.dir[0])
    
    def check_for_food(self):
        for food in world.food:
            dist = (food.x - self.x)**2 + (food.y - self.y)**2
            if dist < Ant.EATING_DISTANCE and food.eaten <= type(food).STATES - 1:
                return food
        return False

    def move(self):
        if time.time() - self.eating_timeout < Ant.EATING_TIMEOUT:
            # eating
            speed = .5
        else:
            speed = 1
        self.x += self.dir[0]*self.speed*camera.delta_t*speed
        self.y += self.dir[1]*self.speed*camera.delta_t*speed

    def update(self):
        
        food = self.check_for_food()
        if food and time.time() - self.eating_timeout > Ant.EATING_TIMEOUT:
            # eat
            food.eat(world)
            world.ants.append(Ant())
            world.score += type(food).POINTS
            self.eating_timeout = time.time()
        self.move()
                
    
    def render(self, screen):
        self.frame_index += camera.delta_t*10
        im = filehandler.get_image(Ant.IMAGE, index=int(self.frame_index % 3))
        _, _, w, h = im.get_rect()
        im = pygame.transform.scale(im, (w*Ant.SIZE, h*Ant.SIZE))
        im, new_rect = rot_center(im, 90-degrees(self.theta), self.x, self.y)
        screen.blit(im, new_rect)
    
    def kill(self):
        world.run_animation(
            DeadAnimation(self.x, self.y)
        )
        world.ants.remove(self)
        if len(world.ants) == 0:
            world.run_animation(
                GameOverAnimation()
            )

world = World()
camera = Camera()
meter = Meter()