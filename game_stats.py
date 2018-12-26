class GameStats():
    """
    Отслеживание статистики для игры Aliens Invasion.
    """
    def __init__(self, ai_settings):
        """
        Инициализирует статистику.
        """
        self.ai_settings = ai_settings
        self.reset_stats()

    # Игра запускается в активном состоянии.
        self.game_active = False

    def reset_stats(self):
        """
        Инициализирует статистику, изменяющуюся в ходе игры.
        """
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
