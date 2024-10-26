from filehandler import filehandler

class FoodItem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.eaten = 0
    
    def render(self, screen):
        im = filehandler.get_image(type(self).IMAGE, index=self.eaten, tile_size=64)
        screen.blit(im, (self.x, self.y))

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