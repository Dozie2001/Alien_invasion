#!/usr/bin/python3
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """OverAll class to manage game behviour"""

    def __init__(self):
        """Initialising game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # Watch for mouse and keyboard movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.key == pygame.K_KEYDOWN:
                self._check_keydown_events(event)
            elif event.key == pygame.K_KEYUP:
                self._check_keyup_events(event)
            # Move the ship to the right.

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # PRESS Q to exit
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the recently most displayed screen visible
        pygame.display.flip()

if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game