"""Uma classe para armazenar todas as configurações da Invasão Alienigena """
class Settings():
    """Inicializa as configurações do jogo"""
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #configuração da espaçonave
        self.ship_speed_factor = 1.5