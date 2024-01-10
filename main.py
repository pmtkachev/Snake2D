import pygame as pg

import src.game_func as gf
from src.food import Apple
from src.snake import Snake

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((300, 300))
pg.display.set_caption('SNAKE 2D')

font = pg.font.Font('fnt/pixel.ttf', 25)

snake, food = Snake(), Apple()

sprites_group = pg.sprite.Group()
gf.sprite_add_group(sprites_group, [snake, food])

game = True

if __name__ == '__main__':
    while True:
        gf.main_menu(font, screen, snake)
        gf.run_game(game, snake, screen, sprites_group, font, food, clock)
