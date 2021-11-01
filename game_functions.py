import sys
import pygame
from bulllet import Bullet
from pygame.sprite import Sprite

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

def update_screen(ai_settings, screen, ship, alien, bullets): #as imagens na tela e alterna para a nova tela.
    # deixa a tela mais recente vísivel
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()#Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    ship.blitme()
    alien.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    # Livra-se dos projéteis que desapareceram
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    #dispara um novo projétil
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)