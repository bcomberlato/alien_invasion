import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        #inicializando o alienigena
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Carrega a imagiem do alienigena e define seu atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #Inicia cada novo alienigina próximo a parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Armazena a posição exata do alienigena
        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image, self.rect)

