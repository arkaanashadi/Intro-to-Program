class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, settings):
        """Initialize statistics."""
        self.game_active = False
        self.settings = settings
        self.reset_stats()
        self.score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
