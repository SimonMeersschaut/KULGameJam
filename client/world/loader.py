import csv
import pygame
from .filehandler import filehandler

TILE_DATA = {}

class Tile:
    def __init__(self, tile_id :int, image_path: str):
        self.tile_id = tile_id
        self.image_path = image_path

    def render_image(self):
        if self.tile_id == -1:
            return None # air
        else:
            return filehandler[self.image_path][self.tile_id]

def load_tiles(filename, image_path: str):
    def get_tile(tile_id: int, tileset: object) -> Tile:
        # check for special tiles
        if tile_id in TILE_DATA:
            # id is a special tile (e.g. entities)
            return TILE_DATA[tile_id]()
        else:
            # id is a default tile (e.g. grass)
            return Tile(tile_id, tileset)
    
    map_data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            map_data.append([get_tile(int(tile_id), image_path) for tile_id in row])
    return map_data

def prerender_map(map_data, tilesize):
    # Create a surface to render the map onto
    im_size = (len(map_data[0]) * tilesize, len(map_data) * tilesize)
    map_surface = pygame.Surface(im_size, pygame.SRCALPHA, 32)

    # Draw the tiles onto the map surface
    for row_idx, row in enumerate(map_data):
        for col_idx, tile in enumerate(row):
            tile_image = tile.render_image()
            if tile_image is not None:
                # do not render if tile is air
                map_surface.blit(tile.render_image(), (col_idx * tilesize, row_idx * tilesize))
    return map_surface