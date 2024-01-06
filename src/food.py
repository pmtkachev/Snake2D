from random import randrange

import pygame as pg


class Apple(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('img/apple.png')
        self.food_pos = {
            'x': randrange(0, 290, 10),
            'y': randrange(0, 290, 10),
        }
        self.rect = self.image.get_rect()
        self.rect.x = self.food_pos['x']
        self.rect.y = self.food_pos['y']

    def update(self, *args):
        self.rect.x = self.food_pos['x']
        self.rect.y = self.food_pos['y']

        if pg.sprite.collide_mask(self, args[0]):
            args[0].snake_tails.append([self.food_pos['x'], self.food_pos['y']])
            self.food_pos = {
                'x': randrange(0, 290, 10),
                'y': randrange(0, 290, 10),
            }
