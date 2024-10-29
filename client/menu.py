import requests
import pygame
from filehandler import filehandler

class Menu:
    def __init__(self):
        with open('resources/naam.txt', 'r') as f:
            self.name = f.read()
        
        data = requests.get('http://94.225.3.78:25565/get_scores').json()

        self.sorted_data = []
        for (name, score) in data.items():
            self.sorted_data.append({'name': name, 'score': score})

        self.sorted_data = sorted(self.sorted_data, key=lambda play: int(play['score']), reverse=True)
    
    def save_name(self):
        with open('resources/naam.txt', 'w') as f:
            f.write(self.name)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_BACKSPACE: 
                self.name = self.name[:-1] 
            else: 
                self.name += event.unicode

    def initialize(self):
        self.font = pygame.font.Font('resources/pixel.ttf', 18)

        self.text_rendered = []
        for i, play in enumerate(self.sorted_data[:5]):
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
        PADDING = 3
        for i, (text1, text2, length) in enumerate(self.text_rendered):
            pygame.draw.rect(screen, (251,229,165), (910 - PADDING, 90 + i*27 - PADDING, 310 + PADDING, 20 + PADDING + 2), border_radius=8)
            screen.blit(text1, (915, 90 + i*27))
            screen.blit(text2, (1200 - (length-1)*10, 90 + i*27))
        
        im = self.font.render('Name: '+self.name, True, (0, 0, 0))
        screen.blit(im, (910, 50))

menu = Menu()