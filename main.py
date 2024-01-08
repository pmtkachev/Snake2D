import pygame as pg

import src.game_func as gf
from src.constants import *
from src.food import Apple
from src.snake import Snake

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.Font('fnt/pixel.ttf', 25)
snake, food = Snake(), Apple()
sprites_group = pg.sprite.Group()
gf.sprite_add_group(sprites_group, [snake, food])

game = True

if __name__ == '__main__':
    while game:

        gf.check_event(snake)

        for i, j in enumerate(snake.snake_tails):
            if (snake.snake_pos['x'] + snake.snake_pos['x_chng'] == snake.snake_tails[i][0]
                and snake.snake_pos['y'] + snake.snake_pos['y_chng'] == snake.snake_tails[i][1]) and \
                    len(snake.snake_tails) >= 4:
                game = False

        screen.fill((153, 204, 3))

        sprites_group.draw(screen)
        sprites_group.update(snake, screen)
        score_str = font.render(f'SCORE: {food.score}', False, 'black')
        snake_2d = font.render(f'SNAKE 2D', False, 'black')
        screen.blits(blit_sequence=((score_str, (15, 5, 0, 0)), (snake_2d, (180, 5, 0, 0))))

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()
    quit()
