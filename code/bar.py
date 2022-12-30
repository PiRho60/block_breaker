import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.Surface((self.settings.PLATFORM_WIDTH,self.settings.PLATFORM_HEIGHT), masks="black")
        self.rect = self.image.get_rect(midbottom=(settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT-100))
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        if (self.moving_left):
            if (self.rect.left > 0):
                self.rect.left -= self.settings.platform_vel
            else:
                self.rect.left = 0
        if (self.moving_right):
            if (self.rect.right < self.settings.SCREEN_WIDTH):
                self.rect.right += self.settings.platform_vel
            else:
                self.rect.right = self.settings.SCREEN_WIDTH