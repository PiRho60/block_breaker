import pygame
from settings import Settings

class Block(pygame.sprite.Sprite):
    settings = Settings()
    image = pygame.Surface((settings.BLOCK_WIDTH,settings.BLOCK_HEIGHT), masks="purple")

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.rect = self.image.get_rect()

    def update(self):
        pass

    @classmethod
    def create_block_group(self, screen):
        block_group = pygame.sprite.Group()

        for i in range(int(self.settings.SCREEN_WIDTH / self.settings.BLOCK_WIDTH)):
            new_block = Block(screen)
            new_block.rect.topleft = (i*self.settings.BLOCK_WIDTH, 0)
            block_group.add(new_block)

        return block_group

