import sys
import pygame
from Alien_Invasion_Attempt_2.Class.bullet import *
from Alien_Invasion_Attempt_2.Class.alien import *
from time import sleep



def check_events(settings, screen, stats, play_button, ship, bullets, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(settings, screen, event, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, play_button, mouse_x, mouse_y, ship, bullets, aliens)


def check_keydown_events(settings, screen, event, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        ship.shooting = True
        fire_bullet(settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_SPACE:
        ship.shooting = False



def update_screen(settings, screen, stats, score_board, play_button, ship, bullets, aliens):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.ship_blitme()
    ship.ship_update(bullets, screen, ship, settings)
    aliens.draw(screen)
    score_board.show_score()

    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    aliens.add(alien)


def create_fleet(settings, stats, screen, aliens, ship):
    alien = Alien(screen)
    print(alien.rect.height)
    number_rows = int(stats.level)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_number_rows(settings, stats,  ship_height, alien_height):
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def update_aliens(settings, stats, screen, ship, bullets, aliens):
    aliens.update(settings)
    check_fleet_edges(settings, aliens)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)


def update_bullets(settings, screen, stats, score_board, ship, bullets, aliens):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings, screen, stats, score_board, ship, aliens, bullets)


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullet(settings, screen, ship)
            bullets.add(new_bullet)


def check_bullet_alien_collisions(settings, screen, stats, score_board, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            score_board.prep_score(settings)

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        stats.level += 1
        create_fleet(settings, stats,  screen, aliens, ship)


def ship_hit(settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        stats.level = 0
        create_fleet(settings, stats, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break


def check_play_button(settings, screen, stats, play_button, mouse_x, mouse_y, ship, bullets, aliens):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)
            stats.game_active = True
            stats.reset_stats()
            aliens.empty()
            bullets.empty()
            create_fleet(settings, stats, screen, aliens, ship)
            ship.center_ship()
