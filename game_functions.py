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


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    #Atualiza a posição dos projéteis e se livra dos projéteis antigos
    #Verifica se algum projétil atingiu os alienígenas
    #Em caso afirmativo, livra-se do projétil e do alienígena
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))

    #Verifica se algum projétil atingiu os alienígenas
    #Em caso afirmativo, livra-se do projétil e do alienígena
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    #Destrói os projéteis existentes e cria uma nova frota
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


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

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #Cria um alienígena e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (alien_width * 2 * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+(alien.rect.height * 2 * row_number)
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    #Cria uma frota completa de alienígenas
    #Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_numbers_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows

def update_aliens(ai_settings, aliens ):
    #Verfica se a frota está em uma das bordas e então atualiza as posições de todos os alinígenas da frota
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def change_fleet_direction(ai_settings, aliens):
    #Faz a frota toda descer e mudar de direção
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



def check_fleet_edges(ai_settings, aliens):
    #Responde apropriadamente se algum alíenigenas alcançou uma borda
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
