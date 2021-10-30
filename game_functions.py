import sys
import pygame
"""Responde a eventos de pressionamento de teclas e de mouse"""
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Move a espaçonave para a direita e para esquerda
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                 ship.moving_left = False

def update_screen(ai_settings, screen, ship): # as imagens na tela e alterna para a nova tela.
    # deixa a tela mais recente vísivel
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()