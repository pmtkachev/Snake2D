import pygame as pg


class Snake(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('img/snake_segment.png')
        self.snake_pos = {'x': 140,
                          'y': 140,
                          'x_chng': 0,
                          'y_chng': 0}
        self.snake_speed = 10
        self.snake_tails = [[self.snake_pos['x'] - 10, self.snake_pos['y']],
                            [self.snake_pos['x'] - 20, self.snake_pos['y']],
                            [self.snake_pos['x'] - 30, self.snake_pos['y']]]
        self.rect = self.image.get_rect()
        self.rect.x = self.snake_pos['x']
        self.rect.y = self.snake_pos['y']

    def update(self, *args):
        self.rect.x = self.snake_pos['x']
        self.rect.y = self.snake_pos['y']

        for tail in self.snake_tails:
            args[1].blit(self.image, (tail[0], tail[1], 10, 10))

        ltx = self.snake_pos['x']
        lty = self.snake_pos['y']

        for i, j in enumerate(self.snake_tails):
            _ltx = self.snake_tails[i][0]
            _lty = self.snake_tails[i][1]

            self.snake_tails[i][0] = ltx
            self.snake_tails[i][1] = lty

            ltx = _ltx
            lty = _lty

        self.snake_pos['x'] += self.snake_pos['x_chng']
        self.snake_pos['y'] += self.snake_pos['y_chng']

        if self.snake_pos['x'] < -10:
            self.snake_pos['x'] = 300
        elif self.snake_pos['x'] > 300:
            self.snake_pos['x'] = 0
        elif self.snake_pos['y'] < -10:
            self.snake_pos['y'] = 300
        elif self.snake_pos['y'] > 300:
            self.snake_pos['y'] = 0
