from filehandler import filehandler
import pygame
import random

class FoodItem:
    SIZE = 64
    def __init__(self):
        self.x = random.randint(0, 1200)
        self.y = random.randint(0, 700)
        self.eaten = 0
    
    def render(self, screen):
        im = filehandler.get_image(type(self).IMAGE, index=self.eaten, tile_size=type(self).SIZE)
        # _, _, w, h = im.get_rect()
        # im = pygame.transform.scale(im, (w*scale, h*scale))
        screen.blit(im, (self.x, self.y))
    
    def eat(self, world):
        # get eaten
        self.eaten += 1
        if self.eaten >= type(self).STATES:
            # entirely eaten
            # remove self
            world.food.remove(self)



#######
class Cookie(FoodItem):
    STATES = 6
    POINTS = 1
    IMAGE = 'resources/images/koekjes.set.png'

class Appelsien(FoodItem):
    STATES = 6
    POINTS = 1
    IMAGE = 'resources/images/sinaasappel.set.png'

class Chip(FoodItem):
    STATES = 10
    POINTS = 1
    IMAGE = 'resources/images/chip.set.png'

class Snoep(FoodItem):
    STATES = 7
    POINTS = 1
    IMAGE = 'resources/images/snoep.set.png'

class Croissant(FoodItem):
    STATES = 9
    POINTS = 1
    IMAGE = 'resources/images/croissant.set.png'

class Bagguette(FoodItem):
    STATES = 7
    POINTS = 1
    IMAGE = 'resources/images/bagguette.set.png'

class Taart(FoodItem):
    STATES = 9
    POINTS = 1
    IMAGE = 'resources/images/taart.set.png'
###

class Apple(FoodItem):
    STATES = 7
    POINTS = 1
    IMAGE = 'resources/images/apple.set.png'

class Pizza(FoodItem):
    STATES = 9
    POINTS = 1
    IMAGE = 'resources/images/pizza.set.png'

class Druif(FoodItem):
    STATES = 7
    POINTS = 4
    IMAGE = 'resources/images/druif.set.png'