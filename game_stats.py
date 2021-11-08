class GameStats():
    #Armazena os dados estatísticos do jogo


    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False


    def reset_stats(self):
        #inicializa os dados estatísticos que podem mudar durante o jogo

        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
