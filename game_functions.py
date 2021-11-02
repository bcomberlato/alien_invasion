import sys
import pygame
from bulllet import Bullet
from alien import Alien


"""Responde a eventos de pressionamento de teclas e de mouse"""
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Move a espaçonave para a direita e para esquerda
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings,screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE: #Cria um novo projétil e o adiciona ao grupo de projéteis
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q: sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, aliens, bullets): #as imagens na tela e alterna para a nova tela.
    # deixa a tela mais recente vísivel
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()#Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    # Livra-se dos projéteis que desapareceram
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    #Dispara um novo projétil
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_numbers_aliens_x(ai_settings, alien_width):
    #Determina o número de alienígenas que cabem em uma linha
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    #Cria um alienígena e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (alien_width * 2 * alien_number)
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    #Cria uma frota completa de alienígenas
    #Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_numbers_aliens_x(ai_settings, alien.rect.width)

    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)