from actor import *

def Platform(Actor):
    def __init__(self, x: int, y: int, width: int, height: int, arena: Arena):
        self._x = x
        self._y = y
        self._w = width
        self._h = height
        self._arena = arena
        arena.add(self)

    def rect(self):
        return self._x, self._y, self._w, self._h
