import pygame as pg
import sys

pg.init()

width = 500
height = 500

clock = pg.time.Clock()

screen = pg.display.set_mode((width, height))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    screen.fill((0, 0, 30))
    pg.display.update()
    clock.tick(60)
