import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init() # Inicializa o pygame, as configurações e o objeto screen
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Cria uma espaçonave
    ship = Ship(ai_settings,screen)
    #define a cor de fundo do jogo
    bg_color = (230,230,230)
    #Inicia o laço principal do jogo
    while True:
        ship.blitme()
        #observa os eventos de teclado e de mouse
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen,ship)
        ship.update()
run_game()