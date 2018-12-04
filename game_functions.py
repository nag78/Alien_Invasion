import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """
    Реагирует на нажатие клавиш.
    """
    if event.key == pygame.K_RIGHT:
        #Переместить корабль вправо.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Переместить корабль влево.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Создание новой пули и включение ее в группу bullets.
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def check_keyup_event(event,ai_settings,screen,ship,bullets):
    """
    Реагирует на отпускание клавиш.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """
    Обрабатывает нажатия клавиш и события мыши.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        #Клавиша отпущена перемещение остановлено
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ai_settings,screen,ship,bullets)

def update_screen(ai_settings,screen,ship,bullets):
    """
    Обновляет изображение на экране и отображает новый экран.
    """
    #При каждом проходе цикла перерисовывает экран.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Отображение последнего прорисованного экрана.
    pygame.display.flip()



