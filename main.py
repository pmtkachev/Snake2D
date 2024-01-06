from random import randrange

import pygame as pg

pg.init()
clock = pg.time.Clock()
scr_width = 300
scr_height = 300

screen = pg.display.set_mode((scr_width, scr_height))

game_end = False

snake_pos = {
    'x': scr_width / 2 - 5,
    'y': scr_height / 2 - 5,
    'x_chng': 0,
    'y_chng': 0
}

snake_speed = 10
snake_tails = []
food_pos = {
    'x': round(randrange(0, scr_width - 10) / 10) * 10,
    'y': round(randrange(0, scr_height - 10) / 10) * 10,
}

while not game_end:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_end = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN and snake_pos['y_chng'] == 0:
                snake_pos['x_chng'] = 0
                snake_pos['y_chng'] = snake_speed
            elif event.key == pg.K_UP and snake_pos['y_chng'] == 0:
                snake_pos['x_chng'] = 0
                snake_pos['y_chng'] = -snake_speed
            elif event.key == pg.K_LEFT and snake_pos['x_chng'] == 0:
                snake_pos['x_chng'] = -snake_speed
                snake_pos['y_chng'] = 0
            elif event.key == pg.K_RIGHT and snake_pos['x_chng'] == 0:
                snake_pos['x_chng'] = snake_speed
                snake_pos['y_chng'] = 0

    screen.fill((110, 171, 130))

    ltx = snake_pos['x']
    lty = snake_pos['y']

    for i, j in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]

        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty

        ltx = _ltx
        lty = _lty

    for t in snake_tails:
        pg.draw.rect(screen, 'black', (t[0], t[1], 10, 10))

    for i, j in enumerate(snake_tails):
        if (snake_pos['x'] + snake_pos['x_chng'] == snake_tails[i][0]
                and snake_pos['y'] + snake_pos['y_chng'] == snake_tails[i][1]):
            print('s')

    snake_pos['x'] += snake_pos['x_chng']
    snake_pos['y'] += snake_pos['y_chng']

    if snake_pos['x'] < -10:
        snake_pos['x'] = scr_width
    elif snake_pos['x'] > scr_width:
        snake_pos['x'] = 0
    elif snake_pos['y'] < -10:
        snake_pos['y'] = scr_height
    elif snake_pos['y'] > scr_height:
        snake_pos['y'] = 0

    if (snake_pos['x'] == food_pos['x']
            and snake_pos['y'] == food_pos['y']):
        snake_tails.append([food_pos['x'], food_pos['y']])

        food_pos = {
            'x': round(randrange(0, scr_width - 10) / 10) * 10,
            'y': round(randrange(0, scr_height - 10) / 10) * 10,
        }

    pg.draw.rect(screen, 'black', (snake_pos['x'], snake_pos['y'], 10, 10))
    pg.draw.rect(screen, 'red', (food_pos['x'], food_pos['y'], 10, 10))
    pg.display.flip()

    clock.tick(10)

pg.quit()
quit()
