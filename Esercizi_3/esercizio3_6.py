import random, game2d, actors

screen_x = screen_y = 500

radius = 15

second_ball_distance = 3 * radius

balls = []

def update():
    game2d.canvas_fill((255,255,255))

    for b in balls:
        b.move_sin()
        x, y, r = b.get_coord()
        game2d.draw_circle((0,0,0),(x,y),(r+2))
        game2d.draw_circle((b.getter()),(x,y),(r))
        

def main():
    global balls
    arena = actors.Arena(screen_x, screen_y)
    balls.append(actors.Ball(0 + radius,arena.get_size()[1]//2,radius,arena))
    balls.append(actors.Ball(0 + radius + second_ball_distance,
                             arena.get_size()[1]//2,radius,arena))

    game2d.canvas_init((arena.get_size()))
    game2d.set_interval(update, 1000//30)

if __name__ == "__main__":
    main()
