#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d

from bounce import Arena, Ball


def setup():
    global arena, turtle, sprites

    arena = Arena(320, 240)
    Ball(arena, 40, 80)
    Ball(arena, 80, 40)

    game2d.canvas_init(arena.size())
    sprites = game2d.image_load("sprites.png")
    
    game2d.set_interval(update, 1000//30)  # millis

def update():
    arena.move_all()  # Game logic

    game2d.canvas_fill((255, 255, 255))
    for a in arena.actors():
        x, y, w, h = a.rect()
        # use the following lines to cut a sprite from a larger image
        xs, ys = a.symbol()
        game2d.image_blit(sprites, (x, y), area=(xs, ys, w, h))    

setup()
