import csv
import pygame
from . import entities

TILE_DATA = {}

class Tile:
    def __init__(self, tile_id :int, tileset: object):
        self.tile_id = tile_id
        self.tileset = tileset
        
        # add custom tile properties
    
    def render_image(self):
        if self.tile_id == -1:
            return None # air
        else:
            return self.tileset[self.tile_id]

def load_csv_map(filename, tileset):
    def get_tile(tile_id: int, tileset: object) -> Tile:
        if tile_id in TILE_DATA:
            return TILE_DATA[tile_id]()
        else:
            return Tile(tile_id, tileset)
    
    map_data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            map_data.append([get_tile(int(tile_id), tileset) for tile_id in row])
    return map_data

# Function to load tileset
def load_tileset(image_path, tile_size):
    tileset = pygame.image.load(image_path).convert_alpha()
    tiles = []
    tileset_width, tileset_height = tileset.get_size()
    for y in range(0, tileset_height, tile_size):
        for x in range(0, tileset_width, tile_size):
            tile = tileset.subsurface((x, y, tile_size, tile_size))
            tiles.append(tile)
    return tiles

def prerender_map(map_data, tileset, tilesize):
    # Create a surface to render the map onto
    map_surface = pygame.Surface((len(map_data[0]) * tilesize, len(map_data) * tilesize), pygame.SRCALPHA, 32)

    # Draw the tiles onto the map surface
    for row_idx, row in enumerate(map_data):
        for col_idx, tile in enumerate(row):
            tile_image = tile.render_image()
            if tile_image is not None:
                # do not render if tile is air
                # tile.render_image()
                map_surface.blit(tile.render_image(), (col_idx * tilesize, row_idx * tilesize))
    return map_surface