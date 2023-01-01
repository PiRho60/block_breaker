import pygame
from settings import Settings

class Block(pygame.sprite.Sprite):
    settings = Settings()

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((self.settings.BLOCK_WIDTH,self.settings.BLOCK_HEIGHT))
        self.rect = self.image.get_rect()

    def update(self):
        pass

    @classmethod
    def create_block_group(self, screen):
        block_group = pygame.sprite.Group()

        colors = [(128,0,128), (255,0,0), (0,255,0), (0,0,255)]
        for j in range (4):
            for i in range(int(self.settings.SCREEN_WIDTH / self.settings.BLOCK_WIDTH)):
                new_block = Block(screen)
                new_block.rect.topleft = (i*self.settings.BLOCK_WIDTH + 2*i + 1, j * self.settings.BLOCK_HEIGHT + 2*j)
                new_block.image.fill(colors[j])
                block_group.add(new_block)

        return block_group

