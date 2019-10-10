import game2d, random

screen_x = screen_y = 500

radius = 15

class Ball():
    def __init__(self, x: int, y: int, radius: int, arena_x: int, arena_y: int):
        self._x, self._y = x, y
        self._radius = radius
        self._dx, self._dy = 5, -5
        self._red = random.randint(0,256)
        self._green = random.randint(0,256)
        self._blue = random.randint(0,256)
        self._arena_x = arena_x
        self._arena_y = arena_y

    def move(self):

        
        if  0 + self._radius < self._x < self._arena_x - self._radius:
            self._x += self._dx
        elif self._x <= 0 + self._radius:
            self._x += 1
        elif self._x >= self._arena_x - self._radius:
            self._x -= 1

        if  0 + self._radius < self._y < self._arena_y - self._radius:
            self._y += self._dy
            self._dy += 0.4
        elif self._y <= 0 + self._radius:
            self._y += 1

        #Questo controllo causa l'effetto di un rimbalzo minuscolo ma continuo :/
        elif self._y >= self._arena_y - self._radius:
            self._y -= 1
            self._dy = 0

    

    def jump(self):    
        self._dy = -5
        
    def go_left(self):
        self._dx = -5
        self._dy = 0
        
    def go_right(self):
        self._dx = 5
        self._dy = 0

    def stay(self):
        self._dx = 0
        self._dy = 0

    def get_coord(self) -> (int, int, int):
        return self._x, self._y, self._radius

    def getter(self) ->(int, int, int):
        return self._red, self._green, self._blue



def keydown(key: str):
    if key == "ArrowRight":
            ball.go_right()
    elif key == "ArrowLeft":
            ball.go_left()
    elif key == "ArrowUp":
            ball.jump()

def keyup(key: str):
    ball.stay()


def update():
    game2d.canvas_fill((255,255,255))

    ball.move()

    x, y, r = ball.get_coord()
    game2d.draw_circle((0,0,0),(x,y),(r+3))
    game2d.draw_circle((ball.getter()),(x,y),(r))

    
ball = Ball(0 + radius + 1, screen_y-radius,radius, screen_x, screen_y)
ball.stay()
game2d.handle_keyboard(keydown, keyup)
game2d.canvas_init((screen_x,screen_y))
game2d.set_interval(update, 1000//30)
