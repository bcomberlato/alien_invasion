import sys
import pygame
from bulllet import Bullet
from alien import Alien
from time import sleep

"""Responde a eventos de pressionamento de teclas e de mouse"""
def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Move a espaçonave para a direita e para esquerda
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    #inicia um novo jogo quando um jogador apertar em play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Reinicia as configurações do jogo
        ai_settings.initialize_dynamic_settings
        #Oculta o cursor do mouse
        pygame.mouse.set_visible(False)
        #Reinicializa os dados estatísticos do jogo
        stats.game_active = True
        stats.reset_stats()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()



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


def update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button):
    #as imagens na tela e alterna para a nova tela.
    # deixa a tela mais recente vísivel
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    ship.blitme()
    aliens.draw(screen)
    scoreboard.show_score()
    if not stats.game_active:
        #desenha o botão Play se o jogo estiver inativo
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, scoreboard, ship, aliens, bullets):
    #Atualiza a posição dos projéteis e se livra dos projéteis antigos

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_collision(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)


def check_bullet_collision(ai_settings, screen, stats, scoreboard, ship, aliens, bullets):
    #Responde a colisões entre projéteis e alienígenas
    #Em caso afirmativo, livra-se do projétil e do alienígena
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += (ai_settings.alien_points * len(aliens))
            scoreboard.prep_score()

    #Destrói projéteis existentes,cria uma nova frota e aumenta a velocidadee do jogo
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ai_settings.increase_speed()


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


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    #Verfica se a frota está em uma das bordas e então atualiza as posições de todos os alinígenas da frota
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


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


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    #Responde ao fato da espaçonave ter sido atingida por um alienígena

    #Decrementa ships_left
    if stats.ship_left > 0:
        stats.ship_left -= 1

        #Esvazia as listas de aliens e projéteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #faz uma pausa
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    #Verifica se algum alienígena alcançou a parte inferior da tela
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break