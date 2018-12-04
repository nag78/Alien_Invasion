import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Инициализируем игру и создаем объект экрана.

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание коробля
    ship = Ship(screen)


    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мыши.
        gf.check_events()
        #При каждом проходе цикла перерисовывается экрае
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()
