import math, actors, game2d

screen_x = screen_y = 500
radius = 10



def update():
    game2d.canvas_fill((255,255,255))
    
    
    ball.move_sin()
    x, y, r = ball.get_coord()
    game2d.draw_circle((0,0,0),(x,y),(r))
    
    game2d.draw_line((150,150,150),(0,arena.get_size()[1]//2),
                     (arena.get_size()[0],arena.get_size()[1]//2))
    


arena = actors.Arena(screen_x,screen_y)
game2d.canvas_init(arena.get_size())    
ball = actors.Ball(0 + radius,arena.get_size()[1]//2,radius,arena)
game2d.set_interval(update, 1000//30)
