import pygame

class Audio:
    def __init__(self):
        self.sounds = {}

    def play(self, filename) -> None:
        """Start playing the sound."""
        # assert filename in self.sounds
        self.sounds[filename].play()
    
    def preload(self, filename: str) -> None:
        self.sounds.update({filename: self.load(filename)})
    
    def load(self, filename: str) -> object:
        return pygame.mixer.Sound(filename)


audio = Audio()