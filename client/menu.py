import requests
import pygame
from filehandler import filehandler

class Menu:
    def __init__(self):
        data = requests.get('http://94.225.3.78:25565/get_scores').json()
        self.sorted_data = sorted(data, key=lambda play: play['score'], reverse=True)

    def initialize(self):
        self.font = pygame.font.Font('resources/pixel.ttf', 20)

        self.text_rendered = []
        for i, play in enumerate(self.sorted_data[:3]):
            self.text_rendered.append(
                (
                    self.font.render(str(play['name']), True, (0, 0, 0)),
                    self.font.render(str(play['score']), True, (0, 0, 0)),
                    len(str(play['score']))
                )
            )
    
    def click(self, pos):
        if 734 > pos[0] > 540 and 499 > pos[1] > 429:
            return True
    
    def render(self, screen):
        # background image
        SCALE = .66667
        im = filehandler.get_image('resources/images/homepage.png')
        _, _, w, h = im.get_rect()
        im = pygame.transform.scale(im, (w*SCALE, h*SCALE))
        screen.blit(im, (0, 0))
        # show scoreboard
        PADDING = 5
        for i, (text1, text2, length) in enumerate(self.text_rendered):
            pygame.draw.rect(screen, (251,229,165), (910 - PADDING, 90 + i*30 - PADDING, 310 + PADDING, 20 + PADDING + 2), border_radius=8)
            screen.blit(text1, (910, 85 + i*30))
            screen.blit(text2, (1200 - (length-1)*8, 85 + i*30))

menu = Menu()