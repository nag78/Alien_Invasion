import sys
import pygame
from bullet import Bullet
from alien import Alien

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
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    """
    Выпускает пулю, если максимум ещё не достгнут.
    """
    #Создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
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

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """
    Обновляет изображение на экране и отображает новый экран.
    """
    #При каждом проходе цикла перерисовывает экран.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    #Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Отображение последнего прорисованного экрана.
    pygame.display.flip()

def update_bullets(bullets):
    """
    Обновляет позицию пуль и уничтожает старые пули
    """
    #Обновление позиции пуль
    bullets.update()
    #Удаление пульб вышедших за пределы экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullet.remove(bullets)
        #print(len(bullets))

def create_fleet(ai_settings,screen,ship,aliens):
    """
    Создает флот пришельцев.
    """
    #Создание пришельца и вычисление количества пришельцев в ряду.
    #Интервал между соседними пришельцами равен одной ширине пришельца.

    alien = Alien(ai_settings,screen)
    number_alien_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
        alien.rect.height)


    #Создание флота пришельцев
    for row_number in range(number_rows):

        for alien_number in range(number_alien_x):
            #Создание пришельца и размещение его в ряду
            create_alien(ai_settings,screen,aliens,alien_number,
                row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """
    Вычисляет количество пришельцев в ряду.
    """
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(avaliable_space_x / (2 * alien_width))

    return number_alien_x

def create_alien(ai_settings, screen,aliens,alien_number, row_number):
    """
    Создает пришельца и размещает его в ряду
    """
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    """
    Определяет количество рядовб помещающихся на экране.
    """
    avaliable_space_y = (ai_settings.screen_height - (3 * alien_height) -
            ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows


def update_aliens (ai_settings,aliens):
    """
    Проверяет достиг ли флот края Экрана.
    Обновляет позиции всех пришельцев во флоте.
    """
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def check_fleet_edges(ai_settings,aliens):
    """
    Реагирует на достижение пришельцами края экрана.
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """
    Опускает весь флот и меняет направление флота.
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1





