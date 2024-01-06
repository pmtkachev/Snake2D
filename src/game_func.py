import pygame as pg


def sprite_add_group(sprite_group, sprite_list):
    for sprite in sprite_list:
        sprite_group.add(sprite)


def check_event(snake):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN and snake.snake_pos['y_chng'] == 0:
                snake.snake_pos['x_chng'] = 0
                snake.snake_pos['y_chng'] = snake.snake_speed
            elif event.key == pg.K_UP and snake.snake_pos['y_chng'] == 0:
                snake.snake_pos['x_chng'] = 0
                snake.snake_pos['y_chng'] = -snake.snake_speed
            elif event.key == pg.K_LEFT and snake.snake_pos['x_chng'] == 0:
                snake.snake_pos['x_chng'] = -snake.snake_speed
                snake.snake_pos['y_chng'] = 0
            elif event.key == pg.K_RIGHT and snake.snake_pos['x_chng'] == 0:
                snake.snake_pos['x_chng'] = snake.snake_speed
                snake.snake_pos['y_chng'] = 0
