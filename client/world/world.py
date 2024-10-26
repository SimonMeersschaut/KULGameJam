import pygame
from . import loader
from filehandler import filehandler
from audio import audio
from .player import player

class World:
    TILE_SIZE = 64
    def __init__(self):
        filehandler.preload_tile_set('resources/images/tiles.set.png', World.TILE_SIZE)
        audio.preload('resources/audio/background.ogg')
        self.load_level(1)
        self.tiles = []
        player.preload_image()
    
    def load_level(self, level_id: int) -> None:
        self.tiles = loader.load_tiles(f'resources/levels/{level_id}.csv', 'resources/images/tiles.set.png')
        self.image = loader.prerender_map(self.tiles, World.TILE_SIZE)
        audio.play('resources/audio/background.ogg')
    
    def render(self, screen: object) -> None:
        """Render the entire world."""
        # render background image
        screen.blit(filehandler['resources/images/background.jpg'], (0,0))
        # render tiles
        screen.blit(self.image, (0, 0))
        # render entities
        player.render(screen)
