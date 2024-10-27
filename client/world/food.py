from filehandler import filehandler
import pygame

class FoodItem:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.eaten = 0
    
    def render(self, screen):
        im = filehandler.get_image(type(self).IMAGE, index=self.eaten, tile_size=64)
        # _, _, w, h = im.get_rect()
        # im = pygame.transform.scale(im, (w*scale, h*scale))
        screen.blit(im, (50, 50))
    
    def eat(self, world):
        # get eaten
        self.eaten += 1
        if self.eaten >= type(self).STATES:
            # entirely eaten
            # remove self
            world.food.remove(self)

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