import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init()#Inicializa o pygame, as configurações e o objeto screen
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Cria uma espaçonave
    ship = Ship(ai_settings, screen)
    #Cria um grupo qual serão armazenados os projetéis
    bullets = Group()
    #Inicia o laço principal do jogo
    while True:
        ship.blitme()
        #observa os eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        #for bullet in bullets.copy():
        #   if bullet.rect.bottom <= 0:
        #       bullet.remove(bullet)
        #   print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()