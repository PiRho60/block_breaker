import pygame

class Settings():
    def __init__(self):
        self.SCREEN_WIDTH = 1080
        self.SCREEN_HEIGHT = 720
        self.platform_vel = 8
        self.ball_vel = 7
        self.FPS = 60

        # Customization
        self.BG_COLOR = (0,153,153)

        # Keybindings
        self.KEY_MOVE_LEFT = pygame.K_a
        self.KEY_MOVE_RIGHT = pygame.K_d
        self.KEY_LAUNCH = pygame.K_SPACE

        # Dimensions
        self.BLOCK_WIDTH = 1080 / 10
        self.BLOCK_HEIGHT = 20

        self.PLATFORM_WIDTH = 120
        self.PLATFORM_HEIGHT = 20
