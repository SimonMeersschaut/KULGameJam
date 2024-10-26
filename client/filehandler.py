import pygame

class FileHandler:
    """Used to load and cache images."""
    def __init__(self):
        self.cache = {}
    
    def __getitem__(self, image_path: str):
        if image_path in self.cache:
            return self.cache[image_path]
        else:
            # load image
            assert '.set.' not in image_path, 'Cannot fetch .set. dynamically.'
            im = self.load_image(image_path)
            self.cache.update({image_path: im})
            return im
    
    def load_image(self, image_path: str) -> object:
        return pygame.image.load(image_path).convert_alpha()

    def preload_tile_set(self, image_path: str, tile_size: int|tuple) -> None:
        if type(tile_size) is int:
            tile_size = (tile_size, tile_size)
        im = self.load_image(image_path)
        tileset_width, tileset_height = im.get_size()
        tileset = [
            im.subsurface((x, y, tile_size[0], tile_size[1]))
            for x in range(0, tileset_width, tile_size[0])
            for y in range(0, tileset_height, tile_size[1])
        ]
        self.cache.update({image_path: tileset})

filehandler = FileHandler()