"""Uma classe para armazenar todas as configurações da Invasão Alienigena """


class Settings():
    """Inicializa as configurações do jogo"""

    def __init__(self):
        #configurações da tela
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #configurações da nave
        self.ship_speed_factor = 1.5
        #Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        

