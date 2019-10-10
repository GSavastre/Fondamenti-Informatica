from actor import *

class Jumper(Actor):
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._w, self._h = 15, 14
        self._speed_x = 2
        self._speed_y = 4.8
        self._dx, self._dy = 0, 0
        self._g = 1.4
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy + self._g
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def repos_y(self, y: int):
        self._y = y
        
    def go_left(self):
        self._dx, self._dy = -self._speed_x, 0
        
    def go_right(self):
        self._dx, self._dy = +self._speed_x, 0

    def go_up(self):
        self._dx, self._dy = 0, -self._speed_y

    def jump(self):
        self._dy = -self._speed_y
        
    def go_down(self):
        self._dx, self._dy = 0, +self._speed_y

    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return (136,3,self._w,self._h)
