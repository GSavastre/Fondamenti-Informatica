import game2d

screen_x = screen_y = 400

class Ball:

    def __init__(self,x: int, y: int):
        self._x = x
        self._y = y
        self._r = 20
        self._dx = 10

    
    def move(self):
        self._x = (self._x + self._dx) % screen_x

    def rect(self) -> (int, int, int):
        return self._x, self._y, self._r

def update():
    global palla
    game2d.canvas_fill((255,255,255))
    palla.move()
    valori_palla = palla.rect()
    game2d.draw_circle((150,150,150),(valori_palla[0],valori_palla[1]),(valori_palla[2]))

def main():
    
    game2d.canvas_init((screen_x,screen_y))
    game2d.set_interval(update, 1000//30)

palla = Ball(screen_x//2,screen_y//2)

if __name__ == "__main__":
    main()

