import sys
import pygame
from Alien_Invasion_Attempt_2.Class.settings import Settings
from Alien_Invasion_Attempt_2.Class.ship import Ship
from Alien_Invasion_Attempt_2 import game_function as gf
from pygame.sprite import Group
from Alien_Invasion_Attempt_2.Class.alien import *
from Alien_Invasion_Attempt_2.Class.game_stats import *
from Alien_Invasion_Attempt_2.Class.button import Button
from Alien_Invasion_Attempt_2.Class.scoreboard import *



def game():

    clock = pygame.time.Clock()
    pygame.init()

    pygame.display.set_caption("Alien Invasion")
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    stats = GameStats(settings)
    ship = Ship(screen)
    score_board = Scoreboard(settings, screen, stats)

    play_button = Button(settings, screen, "Start")

    bullets = Group()

    aliens = Group()

    gf.create_fleet(settings, stats, screen, aliens, ship)

    while True:
        gf.check_events(settings, screen, stats, play_button, ship, bullets, aliens)
        gf.update_screen(settings, screen, stats, score_board, play_button, ship, bullets, aliens)
        if stats.game_active:
            gf.update_screen(settings, screen, stats, score_board, play_button, ship, bullets, aliens)
            gf.update_bullets(settings, screen, stats, score_board, ship, bullets, aliens)
            gf.update_aliens(settings, stats, screen, ship, bullets, aliens)
        else:
            print("gameover")

        clock.tick(60)
        # print(ship.rect)
        # print(ship.rect.right)
        # print(ship.rect.centerx)

game()
