import pygame as pg


class Snake(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('img/snake_segment.png')
        self.rect = self.image.get_rect()
        self.position = {'x': 140,
                         'y': 140,
                         'x_chng': 10,
                         'y_chng': 0}
        self.speed = 10
        self.tail = []

        self.rect.x = self.position['x']
        self.rect.y = self.position['y']

    def update(self, *args):
        self.rect.x = self.position['x']
        self.rect.y = self.position['y']

        for t in self.tail:
            args[1].blit(self.image, (t[0], t[1], 10, 10))

        ltx = self.position['x']
        lty = self.position['y']

        for i, j in enumerate(self.tail):
            _ltx = self.tail[i][0]
            _lty = self.tail[i][1]

            self.tail[i][0] = ltx
            self.tail[i][1] = lty

            ltx = _ltx
            lty = _lty

        self.position['x'] += self.position['x_chng']
        self.position['y'] += self.position['y_chng']

        if self.position['x'] < 20:
            self.position['x'] = 270
        elif self.position['x'] > 270:
            self.position['x'] = 20
        elif self.position['y'] < 40:
            self.position['y'] = 270
        elif self.position['y'] > 270:
            self.position['y'] = 40
