from filehandler import filehandler
import random

class FoodItem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.eaten = 0
    
    def render(self, screen):
        try:
            im = filehandler.get_image(type(self).IMAGE, index=self.eaten, tile_size=64)
            screen.blit(im, (self.x, self.y))
        except:
            print(type(self))
        if random.randint(0, 50) == 0:
            if self.eaten < type(self).STATES - 1:
                self.eaten += 1

class Apple(FoodItem):
    STATES = 7
    IMAGE = 'resources/images/apple.set.png'

class Pizza(FoodItem):
    STATES = 9
    IMAGE = 'resources/images/pizza.set.png'

class Druif(FoodItem):
    STATES = 7
    IMAGE = 'resources/images/druif.set.png'