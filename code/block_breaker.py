import pygame
from settings import Settings
from sys import exit
from bar import Platform
from ball import Ball
from block import Block

def run_game():
    game_active = True
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Block Breaker")
    clock = pygame.time.Clock()

    game_over_font = pygame.font.SysFont("monospace", 50)
    game_over_font.bold = True
    game_over_text_surface = game_over_font.render('Game Over', False, "black")
    game_over_text_rect = game_over_text_surface.get_rect(center=(settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT/6))

    platform_group = pygame.sprite.GroupSingle(Platform(screen, settings))

    block_group = Block.create_block_group(screen)

    ball_group = pygame.sprite.GroupSingle(Ball(screen, settings, platform_group.sprite, block_group))


    while True:
        # Event check
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()
            if game_active:
                if (event.type == pygame.KEYDOWN):
                    if (event.key == settings.KEY_MOVE_LEFT):
                        platform_group.sprite.moving_left = True
                    if (event.key == settings.KEY_MOVE_RIGHT):
                        platform_group.sprite.moving_right = True
                    if (event.key == settings.KEY_LAUNCH and not ball_group.sprite.is_launched):
                        ball_group.sprite.launch()


                if (event.type == pygame.KEYUP):
                    if (event.key == settings.KEY_MOVE_LEFT):
                        platform_group.sprite.moving_left = False
                    if (event.key == settings.KEY_MOVE_RIGHT):
                        platform_group.sprite.moving_right = False
        
        screen.fill(settings.BG_COLOR)

        if game_active:

            platform_group.update()
            platform_group.draw(screen)

            ball_group.update()
            ball_group.draw(screen)
            if (ball_group.sprite.rect.bottom >= settings.SCREEN_HEIGHT):
                game_active = False

            block_group.draw(screen)
        else:
            screen.blit(game_over_text_surface, game_over_text_rect)

        pygame.display.update()

        clock.tick(settings.FPS)



if (__name__ == "__main__"):
    run_game()
