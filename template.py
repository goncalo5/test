#!/usr/bin/env python
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game
GAME_NAME = "My Game"

# Screen
WIDTH = 360
HEIGHT = 480
FPS = 30


class Game(object):
    def __init__(self):

        pygame.init()
        pygame.mixer.init()  # for sound
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(BLACK)
        pygame.display.set_caption(GAME_NAME)
        clock = pygame.time.Clock()

        self.cmd_key_down = False

        self.running = True
        while self.running:
            clock.tick(FPS)
            # Process input (events)
            for event in pygame.event.get():
                self.handle_common_events(event)
            # Update
            # Render (draw)
            self.screen.fill(BLACK)

            pygame.display.flip()

        pygame.quit()

    def handle_common_events(self, event):
        # check for closing window
        if event.type == pygame.QUIT:
            self.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == 310:
                self.cmd_key_down = True
            if self.cmd_key_down and event.key == pygame.K_q:
                self.quit()

        if event.type == pygame.KEYUP:
            if event.key == 310:
                self.cmd_key_down = False

    def quit(self):
        self.running = False


Game()
