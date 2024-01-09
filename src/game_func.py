import pygame as pg


def sprite_add_group(sprite_group, sprite_list):
    for sprite in sprite_list:
        sprite_group.add(sprite)


def check_event(snake):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

        keys = pg.key.get_pressed()

        if keys[pg.K_UP] and snake.snake_pos['y_chng'] == 0:
            snake.snake_pos['x_chng'] = 0
            snake.snake_pos['y_chng'] = -snake.snake_speed
        elif keys[pg.K_DOWN] and snake.snake_pos['y_chng'] == 0:
            snake.snake_pos['x_chng'] = 0
            snake.snake_pos['y_chng'] = snake.snake_speed
        elif keys[pg.K_LEFT] and snake.snake_pos['x_chng'] == 0:
            snake.snake_pos['x_chng'] = -snake.snake_speed
            snake.snake_pos['y_chng'] = 0
        elif keys[pg.K_RIGHT] and snake.snake_pos['x_chng'] == 0:
            snake.snake_pos['x_chng'] = snake.snake_speed
            snake.snake_pos['y_chng'] = 0


def main_menu(font, screen, clock):
    splash = pg.image.load('img/splash.png')
    start_str = font.render('PRESS SPACE', False, (0, 0, 0))
    alph = 255
    start = True
    while start:
        start_str.set_alpha(alph)
        screen.blits(blit_sequence=((splash, (0, 0, 300, 300)), (start_str, (75, 260, 0, 0))))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    start = False
        alph -= 25
        if alph <= 0:
            alph = 255
        clock.tick(10)
        pg.display.flip()


def run_game(game, snake, screen, sprites_group, font, food, clock):
    while game:
        screen.fill((153, 204, 3))

        check_event(snake)

        sprites_group.draw(screen)
        sprites_group.update(snake, screen)
        score_str = font.render(f'SCORE: {food.score}', False, 'black')
        snake_2d = font.render(f'SNAKE 2D', False, 'black')
        disp = pg.image.load('img/disp.png')
        screen.blits(blit_sequence=((score_str, (15, 5, 0, 0)), (snake_2d, (170, 5, 0, 0)),
                                    (disp, (0, 0, 300, 300))))

        for i, j in enumerate(snake.snake_tails):
            if (snake.snake_pos['x'] + snake.snake_pos['x_chng'] == snake.snake_tails[i][0]
                and snake.snake_pos['y'] + snake.snake_pos['y_chng'] == snake.snake_tails[i][1]) and \
                    len(snake.snake_tails) >= 4:
                game = False

        pg.display.flip()
        clock.tick(10)

    snake.snake_pos['x'], snake.snake_pos['y'] = 140, 140
    food.score = 0
    snake.snake_tails = snake.snake_tails[:3]
