import pygame as pg


def sprite_add_group(sprite_group, sprite_list):
    for sprite in sprite_list:
        sprite_group.add(sprite)


def check_event(snake, m):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    keys = pg.key.get_pressed()

    if m == 'game' and keys[pg.K_ESCAPE]:
        return False

    if m == 'menu' and keys[pg.K_SPACE]:
        return False

    if keys[pg.K_UP] and snake.position['y_chng'] == 0:
        snake.position['x_chng'] = 0
        snake.position['y_chng'] = -snake.speed
    elif keys[pg.K_DOWN] and snake.position['y_chng'] == 0:
        snake.position['x_chng'] = 0
        snake.position['y_chng'] = snake.speed
    elif keys[pg.K_LEFT] and snake.position['x_chng'] == 0:
        snake.position['x_chng'] = -snake.speed
        snake.position['y_chng'] = 0
    elif keys[pg.K_RIGHT] and snake.position['x_chng'] == 0:
        snake.position['x_chng'] = snake.speed
        snake.position['y_chng'] = 0
    return True


def main_menu(font, screen, snake):
    start = True
    splash = pg.image.load('img/splash.png')
    start_str = font.render('PRESS SPACE', False, (0, 0, 0))
    alph_ch = 255
    while start:
        start_str.set_alpha(alph_ch)
        screen.blits(blit_sequence=((splash, (0, 0, 300, 300)), (start_str, (75, 260, 0, 0))))
        start = check_event(snake, m='menu')
        alph_ch -= 1

        if alph_ch <= 0:
            alph_ch = 255

        pg.display.flip()


def run_game(game, snake, screen, sprites_group, font, food, clock):
    snake.tail = [[snake.position['x'], snake.position['y']],
                  [snake.position['x'], snake.position['y']],
                  [snake.position['x'], snake.position['y']]]
    while game:
        screen.fill((153, 204, 3))

        sprites_group.draw(screen)
        sprites_group.update(snake, screen)

        score_str = font.render(f'SCORE: {food.score}', False, 'black')
        snake_2d = font.render(f'SNAKE 2D', False, 'black')
        disp = pg.image.load('img/disp.png')
        screen.blits(blit_sequence=((score_str, (15, 5, 0, 0)), (snake_2d, (170, 5, 0, 0)),
                                    (disp, (0, 0, 300, 300))))
        pg.display.flip()

        game = check_event(snake, m='game')

        for i, j in enumerate(snake.tail):
            if (snake.position['x'] == snake.tail[i][0] and snake.position['y'] == snake.tail[i][1]) \
                    and len(snake.tail) >= 4:
                food.score -= len(snake.tail[i:])
                snake.tail = snake.tail[:i]
                break

        clock.tick(10)

    game_over(snake, food)


def game_over(snake, food):
    snake.tail = []
    food.score = 0
    snake.position['x'], snake.position['y'] = 140, 140
