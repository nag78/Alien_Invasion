class Settings():
    """ Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализируем статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 60, 60
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.inicialize_dinamic_settings()

    def inicialize_dinamic_settings(self):
        """ Инициализирует настройки, изменяющиеся в ходе игры.
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction =1 флот движется в право -1 влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости.
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
