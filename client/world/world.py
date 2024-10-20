import pygame
from . import loader



class World:
    TILE_SIZE = 64
    def __init__(self):
        self.load_level(1)
    
    def load_level(self, level_id: int) -> None:
        self.tileset = loader.load_tileset('world/tiles.png', World.TILE_SIZE)
        self.map_data = loader.load_csv_map(f'world/levels/{level_id}.csv', self.tileset)
        self.image = loader.prerender_map(self.map_data, self.tileset, World.TILE_SIZE)