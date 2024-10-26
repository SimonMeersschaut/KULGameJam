from filehandler import filehandler

class Entity:
    def __init__(self, x: float, y: float, image_path: str):
        self.x = x
        self.y = y
        self.image_path = image_path
    
    def preload_image(self):
        _ = filehandler[self.image_path]
    
    def render(self, screen):
        screen.blit(filehandler[self.image_path], (0, 0))


if __name__ == '__main__':
    entity = Entity(0, 0, 'world/tiles.png')
    entity.preload_image()