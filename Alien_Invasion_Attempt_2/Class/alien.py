from pygame.sprite import Sprite
from Alien_Invasion_Attempt_2.Class.settings import *


class Alien(Sprite, Settings):
    """A class to represent a single alien in the fleet."""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load("/Users/Arkaan/PycharmProjects/PygameProjects/Alien_Invasion_Attempt_2/Images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, settings):
        self.x += (settings.alien_speed_factor * settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            print(True)
            return True

        elif self.rect.left <= 0:
            print(True)
            return True
