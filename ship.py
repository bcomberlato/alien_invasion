import pygame

class Ship:
    def __init__(self,ai_settings,screen):
        """Inicializa a espaçonave e define sua posição inicial"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        #Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
    #Atualiza a posição da espaçonave de acordo com a flag de movimento
    #Atualiza o valor do centro da espaçonave, e não o retângulo

        if self.moving_right:
            self.rect.centerx += self.ai_settings.sheep_speed_factor
        if self.moving_left:
            self.rect.centerx -= self.ai_settings.sheep_speed_factor
    #Atualiza o objeto rect de acordo com o self.center
        self.rect.centerx = self.center

    def blitme(self):
    # Desenha a espaçonave em sua posição atua
        self.screen.blit(self.image,self.rect)