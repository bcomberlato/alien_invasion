import pygame
from pygame.sprite import Sprite
"""Uma classe que administra projéteis disparados pelas espaçonaves"""

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
    #cria um objeto para o projetil na posição atual da espaçonave
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,  ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        #move o projetil para cima
        #atualiza a posiçao decimal do projetil
        self.y -= self.speed_factor
        #atualiza a posição de rect
        self.rect.y = self.y
    def draw_bullet(self):
        #desenha o projétil na tela
        pygame.draw.rect(self.screen, self.color, self.rect)
