import pygame

class ImageType:
    default = 0
    tileset = 1    

class FileHandler:
    """Used to load and cache images."""
    def __init__(self):
        self.cache = {}
    
    def load_image(self, image_path: str, size = 1, type: int=0, tile_size=128) -> object:
        if '.set.' in image_path:
            tile_size = (tile_size, tile_size)
            im = pygame.image.load(image_path).convert_alpha()
            tileset_width, tileset_height = im.get_size()
            tileset = [
                im.subsurface((x, 0, tile_size[0], tile_size[1]))
                for x in range(0, tileset_width, tile_size[0])
                # for y in range(0, tileset_height, tile_size[1])
            ]
            self.cache.update({image_path: {"image_type": 1, "size": size, "data": tileset}})
            return tileset
        else:
            # default image
            im = pygame.image.load(image_path).convert_alpha()
            if size != 1:
                _, _, w, h = im.get_rect()
                im = pygame.transform.scale(im, (w*size, h*size))
            self.cache.update({image_path: {"image_type": 0, "size": size, "data": im}})
            return im

    def get_image(self, image_path: str, size=1, index = 0, tile_size = 128):
        if image_path in self.cache:
            if self.cache[image_path]['size'] == size:
                if '.set.' in image_path:
                    return self.cache[image_path]['data'][index]
                else:
                    return self.cache[image_path]['data']
        im = self.load_image(image_path, size, type=1, tile_size=tile_size)
        if '.set.' in image_path:
            return im[index]
        else:
            return im


filehandler = FileHandler()