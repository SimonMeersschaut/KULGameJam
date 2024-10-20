import pygame
from . import loader
from .filehandler import filehandler


class World:
    TILE_SIZE = 64
    def __init__(self):
        filehandler.load_tile_set('world/tiles.set.png', World.TILE_SIZE)
        self.load_level(1)
        self.tiles = []
    
    def load_level(self, level_id: int) -> None:
        self.tiles = loader.load_tiles(f'world/levels/{level_id}.csv', 'world/tiles.set.png')
        self.image = loader.prerender_map(self.tiles, World.TILE_SIZE)
        self.background_image_path = 'world/background.jpg'
    
    def render(self, screen: object) -> None:
        """Render the entire world."""
        # render background image
        screen.blit(filehandler[self.background_image_path], (0,0))
        # render tiles
        screen.blit(self.image, (0, 0))
        # render entities
