from filehandler import filehandler
import pygame

class FoodItem:
    def __init__(self, x=None, y=None):
        self.x = 100
        self.y = 100
        self.eaten = 0
    
    def render(self, screen, scale: float):
        im = filehandler.get_image(type(self).IMAGE, index=self.eaten, tile_size=64)
        _, _, w, h = im.get_rect()
        im = pygame.transform.scale(im, (w*scale, h*scale))
        screen.blit(im, (self.x-32, self.y-32))

class Apple(FoodItem):
    STATES = 7
    POINTS = 10
    IMAGE = 'resources/images/apple.set.png'

class Pizza(FoodItem):
    STATES = 9
    POINTS = 10
    IMAGE = 'resources/images/pizza.set.png'

class Druif(FoodItem):
    STATES = 7
    POINTS = 10
    IMAGE = 'resources/images/druif.set.png'