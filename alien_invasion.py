import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():

    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")

    #Cria uma instancia para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)


    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Cria a frota alienigena
    gf.create_fleet(ai_settings, screen, ship, aliens)


    #Inicia o laço principal do jogo
    while True:
        if stats.game_active:
        #observa os eventos de teclado e de mouse
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

run_game()