from Alien_Invasion_Attempt_2.Class.settings import *
from Alien_Invasion_Attempt_2.Class.bullet import *


class Ship(Settings, Bullet):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load("/Users/Arkaan/PycharmProjects/PygameProjects/AlienInvasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)


        self.moving_right = False
        self.moving_left = False
        self.shooting = False

    def ship_blitme(self):
        self.screen.blit(self.image, self.rect)

    def ship_update(self, bullets, screen, ship, settings):
        if self.moving_right and (self.rect.right <= self.screen_rect.right):
            self.center += self.ship_speed_factor

        elif self.moving_left and self.rect.left >= 0:
            self.center -= self.ship_speed_factor

        self.rect.centerx = self.center

        # if len(bullets) < settings.bullets_allowed:
        #     if self.shooting:
        #         new_bullet = Bullet(settings, screen, ship)
        #         bullets.add(new_bullet)
    def center_ship(self):
        self.center = self.screen_rect.centerx
