import pygame

class FileHandler:
    """Used to load and cache images."""
    def __init__(self):
        self.cache = {}
    
    def load_image(self, image_path: str, size = 1):
        im = pygame.image.load(image_path).convert_alpha()
        if size != 1:
            _, _, w, h = im.get_rect()
            im = pygame.transform.scale(im, (w*size, h*size))
        self.cache.update({image_path: {"size": size, "data": im}})
        return im

    def get_image(self, image_path: str, size=1):
        if image_path in self.cache:
            if self.cache[image_path]['size'] == size:
                return self.cache[image_path]['data']
        im = self.load_image(image_path, size)
        return im


    # def __getitem__(self, image_path: str):
    #     return self.get_image(image_path)

    # def preload_tile_set(self, image_path: str, tile_size: int|tuple) -> None:
    #     if type(tile_size) is int:
    #         tile_size = (tile_size, tile_size)
    #     im = self.load_image(image_path)
    #     tileset_width, tileset_height = im.get_size()
    #     tileset = [
    #         im.subsurface((x, y, tile_size[0], tile_size[1]))
    #         for x in range(0, tileset_width, tile_size[0])
    #         for y in range(0, tileset_height, tile_size[1])
    #     ]
    #     self.cache.update({image_path: tileset})

filehandler = FileHandler()