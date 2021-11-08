import pygame.font
class Button:

    def __init__(self, ai_settings, screen, msg):
        #inicializa os atributos do botão
        self.screen = screen
        #Define as dimensões e as propiedades do botão
        self.screen_rect = screen.get_rect()
        self.width = 200
        self.heigth = 50
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        #Constrói o objeto rect e o centraliza
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = self.screen_rect.center
        #a mensagem deve ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        #Transforma msg em imagem renderizada e centraliza o texto no botão
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #desenha um botão em branco e, em seguida desenha a mensagem
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
