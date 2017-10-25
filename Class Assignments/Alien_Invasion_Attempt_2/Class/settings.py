import pygame


class Settings:
    def __init__(self, s_width=1024,
                 s_height=640,
                 bg_color=(0, 25, 45),
                 ship_speed = 4.5):

        # Screen Settings
        self.screen_width = s_width
        self.screen_height = s_height
        self.bg_color = bg_color


        # Ship Settings
        self.ship_speed_factor = ship_speed
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed_factor = 20
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.score_scale = 1.5


        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 4.5
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 5
        self.fleet_direction = 1
        self.alien_points = 50


    def increase_speed(self):
        # multiplies current speed factors with the speedup_scales
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

