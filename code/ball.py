import pygame
from math import pi, cos, sin

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, settings, platform, block_group):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.platform = platform
        self.block_group = block_group
        self.image = pygame.Surface((18,18), masks="black")
        self.rect = self.image.get_rect(midbottom = platform.rect.midtop)
        self.is_launched = False
        self.velx = 0
        self.vely = 0

    def launch(self):
        self.is_launched = True

        if (self.platform.moving_left):
            self.velx = -self.settings.ball_vel * cos(pi/4)
            self.vely = -self.settings.ball_vel * sin(pi/4)
        elif (self.platform.moving_right):
            self.velx = self.settings.ball_vel * cos(pi/4)
            self.vely = -self.settings.ball_vel * sin(pi/4)
        else:
            self.velx = 0
            self.vely = -self.settings.ball_vel


    def update(self):
        self.update_position()

        self.check_collisions()


    def update_position(self):
        if (not self.is_launched):
            self.rect.midbottom = self.platform.rect.midtop
        else:
            if (self.rect.left <= 0 or self.rect.right >= self.settings.SCREEN_WIDTH):
                self.velx = -self.velx
            if (self.rect.top <= 0 or self.rect.bottom >= self.settings.SCREEN_HEIGHT):
                self.vely = -self.vely

            self.rect.x += self.velx
            self.rect.y += self.vely

    def check_collisions(self):
        self.check_platform_collision()
        self.check_block_collision()
        

    def check_platform_collision(self):
        if (pygame.sprite.collide_rect(self, self.platform)):
            ball_platform_center_displacement = self.rect.centerx - self.platform.rect.centerx
            # Transform displacement of ball from platform's center, in range (-self.settings.PLATFORM_WIDTH/2, self.settings.PLATFORM_WIDTH/2)
            # to the ball's angle, in correcponding range (3pi/4, pi/4)
            angle = pi/2 * (1 - (ball_platform_center_displacement + self.settings.PLATFORM_WIDTH/2)/self.settings.PLATFORM_WIDTH) + pi/4
            
            self.velx = self.settings.ball_vel * cos(angle)
            self.vely = -self.settings.ball_vel * sin(angle)

    def check_block_collision(self):
        if(pygame.sprite.spritecollide(self, self.block_group, True)):
            self.vely = -self.vely

