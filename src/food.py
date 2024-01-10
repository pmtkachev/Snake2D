from random import randrange

import pygame as pg


class Apple(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('img/apple.png')
        self.rect = self.image.get_rect()
        self.position = {
            'x': randrange(30, 260, 10),
            'y': randrange(50, 260, 10),
        }
        self.rect.x = self.position['x']
        self.rect.y = self.position['y']
        self.score = 0

    def update(self, *args):
        self.rect.x = self.position['x']
        self.rect.y = self.position['y']

        if pg.sprite.collide_mask(self, args[0]):
            self.score += 1
            args[0].tail.append([self.position['x'], self.position['y']])
            self.position = {
                'x': randrange(30, 260, 10),
                'y': randrange(50, 260, 10),
            }
